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
    # Using between dates exclusively would only work if the rule always started
    # inside the week that you are looking at. Which should not be likely.
    days_from_rule_start_to_week_start = rule_start_time.days_between(
        week_start_time
    )
    days_from_rule_start_to_week_end = rule_start_time.days_between(
        week_end_time
    )

    if days_from_rule_start_to_week_end < days_from_rule_start_to_week_start:
        furthest_week_bound = week_start_time
    else:
        furthest_week_bound = week_end_time

    # If the furthest boundry of the week is after the start of the rule...
    if furthest_week_bound.int > rule_start_time:
        # ... continue only if the time being tested is smaller (before) than or
        # equal to, the furthest week boundry.
        return testing_time.day_based_int <= furthest_week_bound.day_based_int
    # Otherwise (if the furthest boundry of the week is not after the start of
    # the rule), continue only if the time being tested is greater (after) than
    # or equal to the furthest week boundry.
    return testing_time.day_based_int >= furthest_week_bound.day_based_int

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
    week_end_time.day += NUMBER_OF_DAYS_IN_A_WEEK
    week = Week(week_start_time)

    for rule in rules:
        day = week_start_time.copy()
        for day_in_week in range(NUMBER_OF_DAYS_IN_A_WEEK):
            if rule.start.same_day(day):
                Week[day_in_week][rule.start.event_time_slot] = rule.event
                break
            day.day += 1

        if not rule.intervals[0].is_zero():
            intervals_index = 0
            testing_time = rule.start.copy() + rule.intervals[intervals_index]
            while _continue_checking_intervals(
                    testing_time,
                    rule.start,
                    week_start_time,
                    week_end_time
            ):
                day = week_start_time.copy()
                for day_in_week in range(NUMBER_OF_DAYS_IN_A_WEEK):
                    if testing_time.same_day(day):
                        event_slot = testing_time.event_time_slot
                        Week[day_in_week][event_slot] = rule.event
                intervals_index = (intervals_index + 1) % len(rule.intervals)
                testing_time += rule.intervals[intervals_index]

            intervals_index = -1
            testing_time = rule.start.copy() - rule.intervals[intervals_index]
            while _continue_checking_intervals(
                    testing_time,
                    rule.start,
                    week_start_time,
                    week_end_time
            ):
                day = week_start_time()
                for day_in_week in range(NUMBER_OF_DAYS_IN_A_WEEK):
                    if testing_time.same_day(day):
                        event_slot = testing_time.event_time_slot
                        Week[day_in_week][event_slot] = rule.event
                intervals_index = (intervals_index - 1) % len(rule.intervals)
                testing_time -= rule.intervals[intervals_index]

    return week
