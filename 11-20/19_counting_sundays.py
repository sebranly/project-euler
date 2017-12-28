def is_a_leap_year(year):
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    return False

def get_number_of_days(month, is_a_leap_year):
    if (month == 4 or month == 6 or month == 9 or month == 11):
        return 30
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        return 31
    if is_a_leap_year:
        return 29
    return 28

# Note: for the days, we go from 0 to 6 in order to use the modulo
# Whereas for the months, we go from 1 to 12 for a more conventional notation
# 1 Jan 1900 was a Monday
day_on_1st_day_of_month = 0
number_of_matching_sundays = 0
# From 1900 to 2000
for current_year in range(1900, 2001):
    leap_year = is_a_leap_year(current_year)
    for month in range(1, 13):
        day_on_1st_day_of_month += get_number_of_days(month, leap_year)
        day_on_1st_day_of_month %= 7
        if (day_on_1st_day_of_month == 6 and current_year > 1900 and not (current_year == 2000 and month == 12)):
            number_of_matching_sundays += 1
print(number_of_matching_sundays)
