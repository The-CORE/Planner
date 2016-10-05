from planner.events import Week
from .rule import Rule
from planner import NUMBER_OF_DAYS_IN_A_WEEK
from planner.times import Time

def _continue_checking_intervals(
        testing_time,
        rule_start_time,
        week_start_time,
        week_end_time
):
    # If the testing time is between the rule start time and the furthest week
    # terminator in the direction that the testing time is from the rule start
    # time from the rule start time, return true.

    direction = -1 if testing_time.int < rule_start_time.int else 1
    displacement_of_week_start = (week_start_time.day_based_int \
        - rule_start_time.day_based_int) * direction
    displacement_of_week_end = (week_end_time.day_based_int \
        - rule_start_time.day_based_int) * direction
    if displacement_of_week_end > displacement_of_week_start:
        week_terminator_to_be_between = week_end_time
    else:
        week_terminator_to_be_between = week_start_time
    return (
        rule_start_time.day_based_int <= testing_time.day_based_int <= \
            week_terminator_to_be_between.day_based_int
        or week_terminator_to_be_between.day_based_int <= \
            testing_time.day_based_int <= rule_start_time.day_based_int
    )

def make_week(rules, week_start_time):
    # The event_time_slot of start_time is ignored.
    rules_error = "rules must be a list of rules."
    if not isinstance(rules, (list, tuple)):
        raise TypeError(rules_error)
    for rule in rules:
        if not isinstance(rule, Rule):
            raise TypeError(rules_error)
    if not isinstance(week_start_time, Time):
        raise TypeError("week_start_time must be a Time object.")

    week_start_time.event_time_slot = 0
    week_end_time = week_start_time.copy()
    week_end_time.day += NUMBER_OF_DAYS_IN_A_WEEK - 1
    week = Week(week_start_time)

    for rule in rules:
        day = week_start_time.copy()
        for day_in_week in range(NUMBER_OF_DAYS_IN_A_WEEK):
            if rule.start.same_day(day):
                week[day_in_week][rule.start.event_time_slot] = rule.event
                break
            day.day += 1

        if not rule.intervals[0].is_zero():
            intervals_index = 0
            testing_time = rule.start.copy() + rule.intervals[intervals_index]
            while (
                    _continue_checking_intervals(
                        testing_time,
                        rule.start,
                        week_start_time,
                        week_end_time
                    )
                    and not rule.intervals[intervals_index].is_zero()
            ):
                day = week_start_time.copy()
                for day_in_week in range(NUMBER_OF_DAYS_IN_A_WEEK):
                    if testing_time.same_day(day):
                        event_slot = testing_time.event_time_slot
                        week[day_in_week][event_slot] = rule.event
                    day.day += 1
                intervals_index = (intervals_index + 1) % len(rule.intervals)
                testing_time += rule.intervals[intervals_index]

            intervals_index = -1
            testing_time = rule.start.copy() - rule.intervals[intervals_index]
            while (
                    _continue_checking_intervals(
                        testing_time,
                        rule.start,
                        week_start_time,
                        week_end_time
                    )
                    and not rule.intervals[intervals_index].is_zero()
            ):
                day = week_start_time.copy()
                for day_in_week in range(NUMBER_OF_DAYS_IN_A_WEEK):
                    if testing_time.same_day(day):
                        event_slot = testing_time.event_time_slot
                        week[day_in_week][event_slot] = rule.event
                    day.day += 1
                intervals_index = (intervals_index - 1) % len(rule.intervals)
                testing_time -= rule.intervals[intervals_index]

    return week
