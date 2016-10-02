from planner.times import Time
from planner.times import TimeInterval
from planner.events import Event

# At some point I need to allow for multiple intervals, which it cycles through
# consecutively. That alone would allow for almost all the customising I need.

class Rule:
    def __init__(self, event, start, interval = TimeInterval()):
        if not isinstance(event, Event):
            raise TypeError("event must be an Event object.")
        if not isinstance(start, Time):
            raise TypeError("start must be a Time object.")
        if not isinstance(interval, TimeInterval):
            raise TypeError("interval must be a TimeInterval object.")
        self.event = event
        self.start = start
        self.interval = interval
