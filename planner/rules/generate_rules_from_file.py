RULE_CONTENT_SEPARATOR = "~~"
from .rule import Rule
from planner.times import Time
from planner.times import TimeInterval

def _generate_rule_from_text(text):
    rule_error = ValueError("text cannot be converted to rule.")
    list_ = text.split(RULE_CONTENT_SEPARATOR)

    # If the length of the list does not equal 9 + 4n where n is a non-negative
    # integer, it is not valid.
    if (len(list_) - 9) % 4 != 0 or len(list_) < 9:
        raise rule_error

    event = str(list_[0])

    try:
        start_time = Time(
            int(list_[1]),
            int(list_[2]),
            int(list_[3]),
            int(list_[4])
        )
    except ValueError:
        raise rule_error

    # Number of intervals should always be a whole number.
    number_of_intervals = int((len(list_) - 5) / 4)
    intervals = []
    for interval_number in range(number_of_intervals):
        try:
            interval = TimeInterval(
                int(list_[5 + interval_number * 4]),
                int(list_[5 + interval_number * 4 + 1]),
                int(list_[5 + interval_number * 4 + 2]),
                int(list_[5 + interval_number * 4 + 3])
            )
            intervals.append(interval)
        except ValueError:
            raise rule_error

    return Rule(event, start_time, intervals)

def generate_rules_from_file(directory):
    f = open(directory, "r")
    rules = []
    text = f.readline()
    line = 1
    while text != "":
        try:
            rules.append(_generate_rule_from_text(text))
        except ValueError:
            raise ValueError(
                "Line "
                + str(line)
                + " of "
                + directory
                + " cannot be converted to Rule."
            )
        text = f.readline()
        line += 1
    f.close()
    return rules
