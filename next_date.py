__author__ = "Zelin Cai, Patrick Silvestre"
__license__ = "MIT"

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
months_with_30_days = [4, 6, 9, 11]
months_with_31_days = [1, 3, 5, 7, 8, 10, 12]

def nextDate(date):
    """ Checking if the input is in the format MM/DD/YYYY """
    if date[2] != '/' or date[5] != '/':
        return "ERROR: The input format should be MM/DD/YYYY"

    """ Checking if month is a number"""
    if date[0] not in numbers or date[1] not in numbers:
        return "ERROR: The month needs to be a number"

    """ Checking if day is a number"""
    if date[3] not in numbers or date[4] not in numbers:
        return "ERROR: The day needs to be a number"

    """ Checking if year is a number"""
    if date[6] not in numbers or date[7] not in numbers or date[8] not in numbers or date[9] not in numbers:
        return "ERROR: The year need to be a number"

    next_date = ''
    leap_year = False
    month = int(date[0] + date[1])
    day = int(date[3] + date[4])
    year = int(date[6] + date[7] + date[8] + date[9])

    """ Checking for leap years """
    if year % 4:
        if year % 100:
            if year % 400:
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = True

    """ Checking if the input is within boundaries """
    if month < 1 or month > 12:
        return "ERROR: The month needs to be between 1 to 12"

    if day < 1 or day > 31:
        return "ERROR: The day needs to be between 1 to 31"

    if year < 1900 or year > 2099:
        return "ERROR: The year needs to be between 1900 to 2099"

    """ Checking edge cases """
    if day == 29 and month == 2 and leap_year is False:
        return "ERROR: This year isn't a leap year"

    if day == 31 and month in months_with_30_days:
        return "ERROR: This month only has 30 days"

    """ Checking for end of months """
    if day == 28 and month == 2 and leap_year is True:
        day += 1
    elif day == 28 and month == 2 and leap_year is False:
        day = 1
        month += 1

    if (day == 30 and month in months_with_30_days) or (day == 31 and month in months_with_31_days):
        day = 1
        month += 1

    if day == 31 and month == 12:
        year += 1

    """ Creating result """
    if month < 10:
        next_date += '0' + str(month)
    else:
        next_date += str(month)

    next_date += '/'

    if day < 10:
        next_date += '0' + str(day)
    else:
        next_date += str(day)

    next_date += '/' + str(year)

    return next_date