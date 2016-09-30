from . import days_in_period

def validate_list_date(date):
    if not isinstance(date, list):
        raise TypeError("A list date must be a list.")
    year = str(list_date[0])
    month = str(list_date[1])
    day = str(list(date[2]))
    year = "0" * (4 - len(year)) + year
    month = "0" * (2 - len(month)) + month
    day = "0" * (2 - len(day)) + day
    string_date = str(list_date[0]) + str(list_date[1]) + str(list(date[2]))
    if not valid_string_date(string_date):
        raise ValueError("Invalid date, list dates should be formatted [y,m,d]")

def validate_string_date(date):
    if not valid_string_date(date):
        raise ValueError("Invalid date, dates should be strings formatted 'yyyymmdd'.")

def valid_string_date(date):
    if not isinstance(date, str):
        return False

    date = str(date)

    if len(date) != 8:
        return False

    try:
        int_date = int(date)

        #There was no year zero.
        if int_date < 10101:
            return False

    except ValueError:
        return False

    year = int(date[:4])
    month = int(date [4:6])
    day = int(date[6:])

    if day < 1 or not (0 < month < 13):
        return False

    if day > days_in_period([year, month, day], 1):
        return False

    return True
