from planner.events import Week
from .rule import Rule
from planner import NUMBER_OF_DAYS_IN_A_WEEK
from planner.times import Time

def _between_dates(date, start_date, end_date):
    #Checks if the date is between the other two, inclusively.
    if not isinstance(date, Time):
        raise TypeError("date must be a Time object.")
    if not isinstance(start_date, Time):
        raise TypeError("start_date must be a Time object.")
    if not isinstance(end_date, Time):
        raise TypeError("end_date must be a Time object.")

    days_between_start_and_end = start_date.days_between(end_date)
    days_between_start_and_date = start_date.days_between(date)
    days_between_date_and_end = date.days_between(end_date)

    return (
        days_between_start_and_date <= days_between_start_and_end
        and days_between_date_and_end <= days_between_start_and_end
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
    week_end_time.day += NUMBER_OF_DAYS_IN_A_WEEK
    week = Week()

    for rule in rules:
        day = week_start_time.copy()
        for day_in_week in range(NUMBER_OF_DAYS_IN_A_WEEK):
            if rule.start.same_day(day):
                Week[day_in_week][rule.start.event_time_slot] = rule.event
                break
            day.day += 1

        if not rule.interval.is_zero():
            testing_time = rule.start.copy() + rule.interval
            while _between_dates(testing_time, week_start_time, week_end_time):
                day = week_start_time.copy()
                for day_in_week in range(NUMBER_OF_DAYS_IN_A_WEEK):
                    if testing_time.same_day(day):
                        event_slot = testing_time.event_time_slot
                        Week[day_in_week][event_slot] = rule.event
                testing_time += rule.interval

            testing_time = rule.start.copy() - rule.interval
            while _between_dates(testing_time, week_start_time, week_end_time):
                day = week_start_time()
                for day_in_week in range(NUMBER_OF_DAYS_IN_A_WEEK):
                    if testing_time.same_day(day):
                        event_slot = testing_time.event_time_slot
                        Week[day_in_week][event_slot] = rule.event
                testing_time -= rule.interval

    return week
