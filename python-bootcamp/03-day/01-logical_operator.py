height = int(input("What is your height in cm? "))

if height >= 120:
    print("you can ride")
    age    = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        # print("Children fare amount applicable, pay $5")
    elif age <= 18:
        bill = 7
        # print("pay $7")
    elif age >=45 and age <=55:
        bill = 0
    else:
        bill = 12
        # print("Adult fare amount applicable, pay $12")

    pic = input("Do you want to take a picture? (Y or N) ")
    if pic == "Y":
        if age >= 45 and age <= 55:
            bill = 0
        else:
            bill += 3
    print(f"your total bill is {bill}")

else:
    print('You cant ride')