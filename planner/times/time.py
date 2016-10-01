import math
from planner import validate_limited_integer
from planner import make_integer
from planner import NUMBER_OF_EVENTS_IN_A_DAY
from .utilities import days_in_period

class Time:
    def __init__(self, year, month, day, event_time_slot):
        self.year = year
        # While the event time slot will begin at zero, I could bring myself to
        # do it for the months and days, the computer scientist in me was
        # unfortunately betten by that tiny sliver of common sense that surfaces
        # so rarely within me.
        # The reason I don't just assign the properties here, is becuase I don't
        # want to allow carrying when it is first created, only when it is added
        # to.
        validate_limited_integer(1, 12, month, "month")
        self._month = month
        days_in_month = days_in_period([year, month, 1], 1)
        validate_limited_integer(1, days_in_month, day, "day")
        self._day = day
        validate_limited_integer(
            0,
            NUMBER_OF_EVENTS_IN_A_DAY - 1,
            event_time_slot,
            "event_time_slot"
        )
        self._event_time_slot = event_time_slot

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = make_integer(year, "year")

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        value = make_integer(value, "value")
        if value < 1:
            raise ValueError("month may not be set to less than 1.")
        elif value <= 12:
            self._month = value
        else:
            self._month = (value % 12) + 1
            self.year += math.floor(value / 12)

    @property
    def day(self):
        return self._day

    @property.setter
    def day(self, value):
        value = make_integer(value, "value")
        if value < 1:
            raise ValueError("day may not be set to less than 1.")
        days_in_current_month = days_in_period([self.year, self.month, 1], 1)
        while value > days_in_current_month:
            self.month += 1
            value -= days_in_current_month
            days_in_current_month = days_in_period(
                [self.year, self.month, 1],
                1
            )
        self._day = value

    # Add adding.
