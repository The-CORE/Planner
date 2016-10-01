from .constants import START_DATE
from .constants import START_TIME
from .constants import START_YEAR
from .constants import START_MONTH
from .constants import START_DAY
from .constants import START_LIST

from .utilities import leap_year
from .utilities import days_in_period

from .validation import validate_string_date
from .validation import validate_list_date

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
