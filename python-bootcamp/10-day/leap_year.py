year = int(input("Which year you want to check: "))
month = int(input("Enter a month: "))

def function_in_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year:
        if month == 2:
            days = month_days[month-1] + 1
        else:
            days = month_days[month-1]
    else:
        days = month_days[month-1]
    return days

leap_year = function_in_leap(year)
print(days_in_month(year,month))
