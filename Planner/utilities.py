def leap_year(year):
    try:
        year = int(year)
    except:
        raise ValueError("year must be able to be converted to an int.")
    return (year % 4 == 0 and (not year %  100 == 0 or year % 400 == 0))

def days_in_period(list_date, index):
    #Days in period cannot validate the date. Because validating the date
    #requires that you know the number of days in that period.

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
