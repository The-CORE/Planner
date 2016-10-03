import time
from .time_object import Time

def get_current_day():
    localtime = time.localtime()
    return Time(
        year = localtime[0],
        month = localtime[1],
        day = localtime[2],
        event_time_slot = 0
    )
