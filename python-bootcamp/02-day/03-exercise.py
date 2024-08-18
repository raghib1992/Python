# Ask for user age as input
# Kindly mention the your age in months, weeks and days
age = input("What's your current age? \n")

years_remaining = 60 - int(age)
print(f"Number of years left {years_remaining}")

days_remining = years_remaining * 365
print(f"Number of days left {days_remining}")

week_remaining = years_remaining * 52
print(f"Number of weeks left {week_remaining}")

months_remaning = years_remaining * 12
print(f"Number of months left {months_remaning}")
