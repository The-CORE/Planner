from planner.times import Time
from planner.times import TimeInterval

# At some point I need to allow for multiple intervals, which it cycles through
# consecutively. That alone would allow for almost all the customising I need.

class Rule:
    def __init__(self, event, start, intervals):
        if not isinstance(event, str):
            raise TypeError("event must be a string.")
        if not isinstance(start, Time):
            raise TypeError("start must be a Time object.")
        if not isinstance(intervals, (list, tuple)):
            raise TypeError("intervals must be a list or tuple.")
        for interval in intervals:
            if not isinstance(interval, TimeInterval):
                raise TypeError(
                    "Each item in intervals must be a TimeInterval object."
                )
        self.event = event
        self.start = start
        self.intervals = intervals

        # Intervals is a list of intervals, and, it is assumed that the actual
        # event is situated at the begining of the list. This means that at the
        # time start + intervals[0] there is an event, and at the time start -
        # intervals[len(intervals) - 1] there is an event, and these iterate
        # further in both directions.

        # If intervals[0].is_zero == True, it will be assume that there are no
        # more intervals.
