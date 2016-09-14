STARTDATE = "19700101"
STARTTIME = "0000"
start_year = int(STARTDATE[:4])
start_month = int(STARTDATE[4:6])
start_day = int(STARTDATE[6:])
start_list = [start_year, start_month, start_day]

def leap_year(year):
    return (year % 4 == 0 and (not year %  100 == 0 or year % 400 == 0))

def days_in_period(list_date, index):
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

    #STILL MORE THINGS (esspecially like segmenting it and checking each part.)
    #Useless comment.
