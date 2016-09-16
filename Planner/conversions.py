STARTDATE = "19700101"
STARTTIME = "0000"
start_year = int(STARTDATE[:4])
start_month = int(STARTDATE[4:6])
start_day = int(STARTDATE[6:])
start_list = [start_year, start_month, start_day]

def leap_year(year):
    try:
        year = int(year)
    except:
        raise ValueError("year must be able to be converted to an int.")
    return (year % 4 == 0 and (not year %  100 == 0 or year % 400 == 0))

def days_in_period(list_date, index):
    validate_list_date(list_date)
    #Zero is year, one is month and two is day.
    #This system is used because the date determines how many days are in months and years.
    #And to standardise later functions.
    if index == 0:
        return 366 if leap_year(list_date[0]) else 365
    if index == 1:
        #Feburary
        if list_date[1] == 2:
            return 29 if leap_year(list_date[0]) else 28
        #30 days have september, april, june and july
        elif (
                    list_date[1] == 9
                    or list_date[1] == 4
                    or list_date[1] == 6
                    or list_date[1] == 11
            ):
            return 30
        #All the rest have 31
        else:
            return 31
    else: #index == 2:
        return 1

def date_to_int(string_date):
    #Days since STARTDATE
    return days_between(STARTDATE, string_date)

def days_between(start, end):
    days_between = 0
    start_list = [int(start[:4]), int(start[4:6]), int(start[6:])]
    end_list = [int(end[:4]), int(end[4:6]), int(end[6:])]
    current_list = start_list.copy()
    for index in range(3):
        initial = start_list[index]
        final = end_list[index]
        direction = -1 if final < initial else 1
        for _ in range(initial, final, direction):
            days_between += direction * days_in_period(current_list, index)
            current_list[index] += direction
    return days_between

def validate_list_date(date):
    if not isinstance(date, list):
        raise TypeError("A list date must be a list.")
    year = str(list_date[0])
    month = str(list_date[1])
    day = str(list(date[2])
    year = "0" * (4 - len(year)) + year
    month = "0" * (2 - len(month)) + month
    day = "0" * (2 - len(day)) + day
    string_date = str(list_date[0]) + str(list_date[1]) + str(list(date[2]))
    if not valid_string_date(string_date):
        raise ValueError("Invalid date, list dates should be formatted [y,m,d]")

def validate_string_date(date):
    if not valid_string_date(date):
        raise ValueError("Invalid date, dates should be formatted 'yyyymmdd'.")

def valid_sting_date(date):
    valid = True

    if not isinstance(date, str):
        valid = False

    date = str(date)

    if len(date) != 8:
        valid = False

    try:
        int_date = int(date)

        #There was no year zero.
        if int_date < 10101:
            valid = False

    except ValueError:
        valid = False

    year = int(date[:4])
    month = int(date [4:6])
    day = int(date[6:])

    if day < 1 or not (0 < month < 13):
        valid = False

    if day > days_in_period([year, month, day], 1):
        valid = False

    return valid