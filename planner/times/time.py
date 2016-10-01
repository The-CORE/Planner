import math
from planner import validate_limited_integer
from planner import make_integer
from planner import NUMBER_OF_EVENTS_IN_A_DAY
from .utilities import days_in_period

class Time:
    def __init__(self, year, month, day, event_time_slot):
        # While the event time slot will begin at zero, I could bring myself to
        # do it for the months and days, the computer scientist in me was
        # unfortunately betten by that tiny sliver of common sense that surfaces
        # so rarely within me.
        self.year = year
        # The reason I don't just assign the properties here, is becuase I don't
        # want to allow carrying when it is first created, only when it is added
        # to.

        # The premise of the months and days is modular arithmatic, such that 0,
        # as there is no actual 0 month or day, is the last value.
        # The original setting will be in the form the user will understand.
        validate_limited_integer(1, 12, month, "month")
        self._month = month % 12
        days_in_month = days_in_period([year, month, 1], 1)
        validate_limited_integer(1, days_in_month, day, "day")
        self._day = day % days_in_month
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
        value = make_integer(value)
        if value == 0:
            raise ValueError("year may not be set to 0.")
        self._year = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        value = make_integer(value)
        if value == 0:
            raise ValueError("month may not be set to 0.")
        direction = 0 if value == 0 else abs(value) / value
        while not 1 <= value <= 12:
            if abs(self.year) == 1 and direction != self.year:
                # If moving one in this direction would put the year at zero...
                self.year += 2 * direction
                # Skip it. There is no zero year.
            else:
                self.year += direction
            value -= direction * 12
        self._month = value

    @property
    def day(self):
        return self._day

    @property.setter
    def day(self, value):
        value = make_integer(value)
        if value == 0:
            raise ValueError("day may not be set to 0.")
        direction = 0 if value == 0 else abs(value) / value
        days_in_current_month = days_in_period([self.year, self.month, 1], 1)
        while not 1 <= value <= days_in_current_month:
            if self.month == 1 and direction == -1
                self.month += 2 * direction
            else:
                self.month += direction
            value -= direction * days_in_current_month
            days_in_current_month = days_in_period(
                [self.year, self.month, 1],
                1
            )
        self._day = value

    @property
    def event_time_slot(self):
        return self._event_time_slot

    @event_time_slot.setter
    def event_time_slot(self, value):
        value = make_integer(value)
        # If value is zero, direction will never be used anyway.
        direction = 0 if value == 0 else abs(value) / value
        while not 0 <= value <= NUMBER_OF_EVENTS_IN_A_DAY:
            self.day += direction
            value -= direction * NUMBER_OF_EVENTS_IN_A_DAY
        self._event_time_slot = value

    def __add__(self, value_to_add):
        if not isinstance(value_to_add, Time):
            return NotImplemented
