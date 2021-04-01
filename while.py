number = 6

while True:
    user_input = input("WOuld you like to play this game? (Y/n)  ")

    if user_input == "n":
        print("better luck next time")
        break

    user_number = int(input("Guess the correct number to won the Merceedes car: "))

    if user_number == number:
        print("You wont the car")
    elif abs(user_number - number) == 1:
        print("you miss it by 1 number, press y to play again")
    else:
        print("Haar gaile..bhak iha se")