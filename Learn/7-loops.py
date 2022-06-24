number = 7

ask = input("Would you like to play a number game? (Y/n) ")

while ask != "n":
    user_input = int(input("Guess the number? "))
    if user_input == number:
        print("Correct!, you won the bouronvita gift hampper")
    elif (number - user_input) in (1, -1):
        print ("you are close")
    else:
        print ("Better Luck Next Time")
    ask = int(input("Would you like to play again? "))

#######################################

number = 7

while True:
    
    ask = input("Would you like to play a number game? (Y/n) ")

    if ask == "n":
        break
    
    user_input = int(input("Guess the number? "))
    if user_input == number:
        print("Correct!, you won the bouronvita gift hampper")
    elif (number - user_input) in (1, -1):
        print ("you are close")
    else:
        print ("Better Luck Next Time")
#############################################
friends = ["Zaman", "Israr", "Waquar"]

for friend in friends:
    print(f"{friend} is my friend")
# ############################################# 
# for number in range(10):
#     print(f"{number}")