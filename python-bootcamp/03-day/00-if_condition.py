# if else condition
# Condition for roller coaster ride is, height of rider should be greater than 120 cm

# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("you can ride")
# else:
#     print('You cant ride')


# Nested if and else condition
# Age of rider more than 18 years should pay adult fare Rs 300 otherwse pay childer fare Rs 150
height = int(input("What is your height in cm? "))


# if height >= 120:
#     print("you can ride")
#     age    = int(input("What is your age? "))
#     if age <= 18:
#         print("Children fare amount applicable")
#     else:
#         print("Adult fare amount applicable")
# else:
#     print('You cant ride')


# Nested if, else and elif condiiton
# For age less than 18 pay $5, for age 18 pay $7 and for more than age 18 pay $12
# if height >= 120:
#     print("you can ride")
#     age    = int(input("What is your age? "))
#     if age < 18:
#         print("Children fare amount applicable, pay $5")
#     elif age == 18:
#         print("pay $7")
#     else:
#         print("Adult fare amount applicable, pay $12")
# else:
#     print('You cant ride')

# Multiple if condition
if height >= 120:
    print("you can ride")
    age    = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        # print("Children fare amount applicable, pay $5")
    elif age <= 18:
        bill = 7
        # print("pay $7")
    else:
        bill = 12
        # print("Adult fare amount applicable, pay $12")

    pic = input("Do you want to take a picture? (Y or N) ")
    if pic == "Y":
        bill += 3
    print(f"your total bill is {bill}")

else:
    print('You cant ride')
