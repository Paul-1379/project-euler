def is_leap_year(year):
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

def get_day_number_in_month(month, year):
    if month == 9 or month == 4 or month == 6 or month == 11:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31
    
year = 1900
month = 1
week_day = 0
month_day = 0
first_month_sunday = 0

while year < 2001:
    week_day = (week_day + 1)%7
    if month_day == get_day_number_in_month(month, year):
        month += 1
        if month == 13:
            month = 1
            year += 1
        month_day = 1
    else:
        month_day += 1

    if week_day == 6 and month_day ==1 and year > 1900:
        first_month_sunday += 1

print(first_month_sunday)