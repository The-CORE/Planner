#from . import display

from . import utilities

NUMBER_OF_EVENTS_IN_A_DAY = 48
NUMBER_OF_DAYS_IN_A_WEEK = 7

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

START_TIME = TimeConstant(1970, 1, 1, 0)

from . import events
from . import rules
from . import times
