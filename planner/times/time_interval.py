from planner.utilities import make_integer

class TimeInterval:
    # This class is simply a holder for years, months, days and event_time_slots
    # Designed to be able to be added and subtracted to/from the Time object.

    def __init__(self, years, months, days, event_time_slots):
        self.years = make_integer(years, "years")
        self.months = make_integer(months, "months")
        self.days = make_integer(days, "days")
        self.event_time_slots = make_integer(
            event_time_slots,
            "event_time_slots"
        )

    # The below properties are for addition with Time objects.

    @property
    def year(self):
        return self.years

    @property
    def month(self):
        return self.months

    @property
    def day(self):
        return self.days

    @property
    def event_time_slot(self):
        return self.event_time_slots
