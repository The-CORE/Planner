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
        # The reason I don't just assign the properties here, is becuase I don't
        # want to allow carrying when it is first created, only when it is added
        # to.
        year = make_integer(year, "year")
        if year == 0:
            raise ValueError("year may not be set to 0.")
        self._year = year
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
        value = make_integer(value)
        if value == 0:
            # Rather than refusing to allow the year to be set to zero, it will
            # be set to the next value in the direction away from the previous
            # value. i.e. -1 if the old value was positive, 1 if the old value
            # was negative. This is so addition and subtraction can work with
            # the year value.
            # This may create some unexpected behaviour, but, I think this is
            # the best way to do this.
            # Also, the old value is known to not be zero due to previous
            # validation
            old_sign = int(abs(self.year) / self.year)
            value = -old_sign
        self._year = value

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        value = make_integer(value)
        if value == 0:
            # See this section in the year setter for justification.
            # Setting the month to 0 is the equivalent of setting it to twelve
            # in the previous year.
            self.year -= 1
            value = 12
        direction = 0 if value == 0 else int(abs(value) / value)
        while not 1 <= value <= 12:
            self.year += direction
            value -= direction * 12
        self._month = value
        # However, the days may not fit in this month.
        # This will recure, but should never happen more than once, but, I guess
        # I am accounting for possible errors elsewhere.
        # The implications of doing this are, that, if you add to the month, the
        # days may overflow, increasing the month by two, in fact.
        days_this_month = days_in_period([self.year, self.month, 1], 1)
        if self.day > days_this_month:
            self.day -= days_this_month
            self.month += 1

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        # So that when increasing the month it doesn't roll over because there
        # are too many for that month, when we are in fact setting it to
        # something acceptable.
        self._day = 1
        value = make_integer(value)
        if value == 0:
            # See this section in the year setter for justification.
            # Setting the day to zero is the equivalent of setting it to the
            # last day in the previous month.
            self.month -= 1
            value = days_in_period([self.year, self.month, 1], 1)
        direction = 0 if value == 0 else int(abs(value) / value)
        days_in_current_month = days_in_period([self.year, self.month, 1], 1)
        while not 1 <= value <= days_in_current_month:
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
        direction = 0 if value == 0 else int(abs(value) / value)
        while not 0 <= value <= NUMBER_OF_EVENTS_IN_A_DAY:
            self.day += direction
            value -= direction * NUMBER_OF_EVENTS_IN_A_DAY
        self._event_time_slot = value

    def copy(self):
        return Time(self.year, self.month, self.day, self.event_time_slot)

    def __add__(self, value_to_add):
        if not isinstance(value_to_add, Time):
            return NotImplemented
        copy = self.copy()
        copy.event_time_slot += value_to_add.event_time_slot
        copy.day += value_to_add.day
        copy.month += value_to_add.month
        copy.year += value_to_add.year
        return copy

    def __sub__(self, value_to_sub):
        if not isinstance(value_to_sub, Time):
            return NotImplemented
        copy = self.copy()
        copy.event_time_slot -= value_to_sub.event_time_slot
        copy.day -= value_to_sub.day
        copy.month -= value_to_sub.month
        copy.year += value_to_sub.year
        return copy

    def __repr__(self):
        return "Time({}, {}, {}, {})".format(
            self.year,
            self.month,
            self.day,
            self.event_time_slot
        )
