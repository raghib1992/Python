# While
# number = 7

# ask = input("Would you like to play a number game? (Y/n) ")

# while ask != "n":
#     user_input = int(input("Guess the number? "))
#     if user_input == number:
#         print("Correct!, you won the bouronvita gift hampper")
#     elif (number - user_input) in (1, -1):
#         print ("you are close")
#     else:
#         print ("Better Luck Next Time")
#     ask = int(input("Would you like to play again? "))

#######################################
x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('x==3')
        break
    else:
        print('continuing...')
        # continue
else:
    print("Done here!!! ")
# number = 7

# while True:
    
#     ask = input("Would you like to play a number game? (Y/n) ")

#     if ask == "n":
#         break
    
#     user_input = int(input("Guess the number? "))
#     if user_input == number:
#         print("Correct!, you won the bouronvita gift hampper")
#     elif (number - user_input) in (1, -1):
#         print ("you are close")
#     else:
#         print ("Better Luck Next Time")
#############################################
# For
# friends = ["Zaman", "Israr", "Waquar"]

# for friend in friends:
#     print(f"{friend} is my friend")
# ############################################# 
# for number in range(10):
#     if number % 2 == 0:
#         print(f"The number is even number {number}")
#     else:
#         print(f"The number is odd number {number}")

for n in range(0,20,2):
    print(n)

