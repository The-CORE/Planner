def event_time_slot_to_time(event_time_slot):
    time = str(event_time_slot / 2)
    time = time.split(".")
    if time[1] == "5":
        time = time[0]
        if len(time) == 1:
            time = "0" + time
        time += "30"
    else:
        time = time[0]
        if len(time) == 1:
            time = "0" + time
        time += "00"
    return time

#import .graphic
from .text import render
