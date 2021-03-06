from .time_object import Time
from .time_interval import TimeInterval
from .get_current_day import get_current_day

from planner import START_TIME

from planner.utilities import leap_year
from planner.utilities import days_in_period

def date_to_int(string_date):
    #Days since STARTDATE
    return days_between(START_DATE, string_date)

def days_between(start, end):
    validate_string_date(start)
    validate_string_date(end)
    days_between = 0
    start_list = [int(start[:4]), int(start[4:6]), int(start[6:])]
    end_list = [int(end[:4]), int(end[4:6]), int(end[6:])]
    current_list = start_list.copy()
    for index in range(3):
        initial = start_list[index]
        final = end_list[index]
        direction = -1 if final < initial else 1
        for _ in range(initial, final, direction):
            days_between += direction * days_in_period(current_list, index)
            current_list[index] += direction
    return days_between
