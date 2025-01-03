def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def days_in_month(year, month):
#
# Your code from LAB 4.3.1.7.
#
    if month < 1 or month > 12 or year < 1:
        return None

    # Days in each month
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Adjust for leap year
    if month == 2 and is_year_leap(year):
        return 29

    return days_in_months[month - 1]

def day_of_year(year, month, day):
#
# Write your new code here.
#
    if month < 1 or month > 12 or day < 1:
        return None

    total_days = 0
    for m in range(1, month):
        days = days_in_month(year, m)
        if days is None:
            return None
        total_days += days

    days_in_current_month = days_in_month(year, month)
    if days_in_current_month is None or day > days_in_current_month:
        return None

    total_days += day
    return total_days

# DOY Calendar
print(day_of_year(2000, 9, 30))