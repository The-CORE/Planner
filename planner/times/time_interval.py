from planner.utilities import make_integer

class TimeInterval:
    # This class is simply a holder for years, months, days and event_time_slots
    # Designed to be able to be added and subtracted to/from the Time object.

    def __init__(self, years = 0, months = 0, days = 0, event_time_slots = 0):
        self.years = get_validated_non_negative_integer(years, "years")
        self.months = get_validated_non_negative_integer(months, "months")
        self.days = get_validated_non_negative_integer(days, "days")
        self.event_time_slots = get_validated_non_negative_integer(
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

    def is_zero(self):
        return (
            self.years == 0
            and self.months == 0
            and self.days == 0
            and self.event_time_slots == 0
        )
