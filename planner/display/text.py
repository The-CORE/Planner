from planner.events import Week
from planner import NUMBER_OF_DAYS_IN_A_WEEK
from planner import NUMBER_OF_EVENTS_IN_A_DAY
import math

SCREEN_WIDTH = 80
#SCREEN_HEIGHT = 25
WIDTH_FOR_EVENT_SLOT = 4
# Number of days in a week is subtracted again at the end, to account for the
# the separators.
WIDTH_FOR_DAY = int((SCREEN_WIDTH - WIDTH_FOR_EVENT_SLOT) \
    / NUMBER_OF_DAYS_IN_A_WEEK) - NUMBER_OF_DAYS_IN_A_WEEK
VERTICAL_SEPARATOR = "-"
HORIZONTAL_SEPARATOR = "|"
EMPTY_CHARACTER = " "
NEW_LINE = "\n"

def _make_length(string, length):
    string = str(string)[:length]
    while len(string) < length:
        string.append(EMPTY_CHARACTER)

def render(week):
    if not isinstance(week, Week):
        raise TypeError("week must be a Week object.")
    first_line = EMPTY_CHARACTER * WIDTH_FOR_EVENT_SLOT
    day = week.start.copy()
    for day_in_week in range(NUMBER_OF_DAYS_IN_A_WEEK):
        first_line += _make_length(
            HORIZONTAL_SEPARATOR + day.string_date,
            WIDTH_FOR_DAY
        )
        day.day += 1
    for event_time_slot in range(NUMBER_OF_EVENTS_IN_A_DAY):
        line = _make_length(str(event_time_slot), WIDTH_FOR_EVENT_SLOT)
        for day in week.days:
            line += _make_length(day[event_time_slot], WIDTH_FOR_DAY
        print(line)
