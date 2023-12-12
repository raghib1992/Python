def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def days_in_month(year,month):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2:
        if is_leap(year):
            print(f"Number of days in {month} in {year} is 28")
        else:
            print(f"Number of days in {month} in {year} is 29")
    else:
        print(f"Number of days in {month} in {year} is {months[month+1]}")

days_in_month(int(input("Input year: ")), int(input("Input month: ")))