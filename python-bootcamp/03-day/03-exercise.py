# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

# Check for leap year, ask for input
year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("This year is leap year")
#         else:
#             print("This year is not leap year")
#     else:
#         print("this year is leap year")
# else:
#     print("This year is not leap year")

if year % 4 == 0 & year % 100 == 0 & year % 400 == 0:
    print("This year is leap year")
else:
    print("This year is not leap year")
    