def validate_limited_integer(lower_limit, upper_limit, value, name_of_value):
    error_message = str(name_of_value) + " must be an integer between " \
        + str(lower_limit) + " and " + str(upper_limit) + " (inclusive)."
    if not isinstance(value, int):
        raise TypeError(error_message)
    if not lower_limit <= value <= upper_limit:
        raise ValueError(error_message)

def make_integer(value, name = "value"):
    try:
        return int(value)
    except ValueError:
        raise ValueError(str(name) + "must be, or be convertable to, an int.")
