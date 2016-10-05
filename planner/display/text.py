from planner.events import Week
from planner import NUMBER_OF_DAYS_IN_A_WEEK
from planner import NUMBER_OF_EVENTS_IN_A_DAY
from planner.display import event_time_slot_to_time
import math

SCREEN_WIDTH = 80
#SCREEN_HEIGHT = 25
WIDTH_FOR_EVENT_SLOT = 4
# Number of days in a week is subtracted again at the end, to account for the
# the separators.
WIDTH_FOR_DAY = int((SCREEN_WIDTH - WIDTH_FOR_EVENT_SLOT) \
    / NUMBER_OF_DAYS_IN_A_WEEK)
VERTICAL_SEPARATOR = "-"
HORIZONTAL_SEPARATOR = "|"
EMPTY_CHARACTER = " "
NEW_LINE = "\n"
DAY_MONTH_DATE_STYLE_THRESHOLD = 11

def _make_length(string, length):
    string = str(string)[:length]
    while len(string) < length:
        string += EMPTY_CHARACTER
    return string

def render(week):
    if not isinstance(week, Week):
        raise TypeError("week must be a Week object.")
    first_line = EMPTY_CHARACTER * WIDTH_FOR_EVENT_SLOT
    day = week.start.copy()
    for day_in_week in range(NUMBER_OF_DAYS_IN_A_WEEK):
        if WIDTH_FOR_DAY >= DAY_MONTH_DATE_STYLE_THRESHOLD:
            day_string = day.string_date
        else:
            day_string = day.string_date_day_month
        first_line += _make_length(
            HORIZONTAL_SEPARATOR + day_string,
            WIDTH_FOR_DAY
        )
        day.day += 1
    print(first_line)
    for event_time_slot in range(NUMBER_OF_EVENTS_IN_A_DAY):
        line = _make_length(
            str(event_time_slot_to_time(event_time_slot)),
            WIDTH_FOR_EVENT_SLOT
        )
        for day in week.days:
            line += _make_length(
                HORIZONTAL_SEPARATOR + day[event_time_slot], WIDTH_FOR_DAY
            )
        print(line)
