def function_in_leap(year):
    """Check for leap year"""
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
    
year = int(input("Enter year: "))
function_in_leap(year)