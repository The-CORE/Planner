from planner import NUMBER_OF_DAYS_IN_A_WEEK
from .day import Day

class Week:
    def __init__(self):
        self._days = []
        for i in range(NUMBER_OF_DAYS_IN_A_WEEK):
            self._days.append(Day())

    def __getitem__(self, key):
        return self._days[key]
