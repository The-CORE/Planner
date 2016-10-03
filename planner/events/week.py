from planner import NUMBER_OF_DAYS_IN_A_WEEK
from .day import Day
from planner.times import Time

class Week:
    def __init__(self, start):
        if not isinstance(start, Time):
            raise TypeError("start must be a time object.")
        # The event_time_slot is ignored.
        start.event_time_slot = 0
        self.start = start
        self.days = []
        for i in range(NUMBER_OF_DAYS_IN_A_WEEK):
            self.days.append(Day())

    def __getitem__(self, key):
        return self.days[key]
