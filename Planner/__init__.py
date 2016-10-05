NUMBER_OF_EVENTS_IN_A_DAY = 48
NUMBER_OF_DAYS_IN_A_WEEK = 7

from . import utilities

class TimeConstant:
    def __init__(self, year, month, day, event_time_slot):
        year = utilities.make_integer(year, "year")
        if year == 0:
            raise ValueError("year may not be set to 0.")
        self.year = year
        utilities.validate_limited_integer(1, 12, month, "month")
        self.month = month
        days_in_month = utilities.days_in_period([year, month, 1], 1)
        utilities.validate_limited_integer(1, days_in_month, day, "day")
        self.day = day
        utilities.validate_limited_integer(
            0,
            NUMBER_OF_EVENTS_IN_A_DAY - 1,
            event_time_slot,
            "event_time_slot"
        )
        self.event_time_slot = event_time_slot

    def __repr__(self):
        return "Time({}, {}, {}, {})".format(
            self.year,
            self.month,
            self.day,
            self.event_time_slot
        )

START_TIME = TimeConstant(1970, 1, 1, 0)
RULES_FILE = "rules.txt"

from . import events
from . import rules
from . import times
from . import display

current_date = times.get_current_day()
try:
    rules_list = rules.generate_rules_from_file(RULES_FILE)
except (FileNotFoundError, ValueError):
    raise ValueError("Invalid or non-existent rules file.")
week = rules.make_week(rules_list, current_date)
display.render(week)
