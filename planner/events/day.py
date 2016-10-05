from planner.utilities import validate_limited_integer
from planner import NUMBER_OF_EVENTS_IN_A_DAY

EMPTY_EVENT = ""

class Day:
    def __init__(self):
        self._events = []
        for _ in range(NUMBER_OF_EVENTS_IN_A_DAY):
            self._events.append(EMPTY_EVENT)

    def add_event(self, event, time):
        if not isinstance(event, str):
            raise TypeError("event must be a string.")
        validate_limited_integer(0, NUMBER_OF_EVENTS_IN_A_DAY - 1, time, "time")
        self._events[time] = event

    def get_event_at_time(self, time):
        validate_limited_integer(0, NUMBER_OF_EVENTS_IN_A_DAY - 1, time, "time")
        return self._events[time]

    def __getitem__(self, key):
        return self._events[key]

    def __setitem__(self, key, value):
        if not isinstance(value, str):
            raise TypeError("Day objects can only hold strings (events).")
        self._events[key] = value
