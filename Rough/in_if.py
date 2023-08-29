number = 7

user_input = (input("pls press 'y' if you want to play: ")).lower()

if user_input == "y":
    user_number = int(input("Guess the number behind the board to win Merceedes car: "))
    if user_number == number:
        print("You won the Jacpot")
    elif abs(user_number - number) == 1:
        print("you are missed it by 1 number")
    else:
        print("Pls try next time")

else:
    print("Thankyou, hope you try ths amazing game of guessing number next time")