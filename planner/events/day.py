from . import validate_limited_integer
from .event import Event

_NUMBER_OF_EVENTS_IN_DAY = 48

class Day:
    def __init__(self):
        self._events = []
        for _ in range(_NUMBER_OF_EVENTS_IN_DAY):
            self._events.append(None)

    def add_event(self, event, time):
        if not isinstance(event, Event):
            raise TypeError("event must be an Event object.")
        validate_limited_integer(0, _NUMBER_OF_EVENTS_IN_DAY - 1, time, "time")
        self._events[time] = event

    def get_event_at_time(self, time):
        validate_limited_integer(0, _NUMBER_OF_EVENTS_IN_DAY - 1, time, "time")
        return self._events[time]

    def __getitem__(self, key):
        return self._events[key]

    def __setitem__(self, key, value):
        if not isinstance(event, Event):
            raise TypeError("Day objects can only hold events.")
        self._events[key] = value
