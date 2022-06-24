from tkinter import N


f = ['a', 'b', 'c']
print('a' in f)

movies_watched = {"Titanic", "Edge Of Tomorrow", "Matrix"}
user_movie = input("Enter something you've watched recently: ")

print(user_movie in movies_watched)

#######################

number = 7

ask = input("Would you like to play a number game? 'y' ")

if ask in ('Y', 'y'):
    user_input = int(input("Guess the number? "))
    if user_input == number:
        print("Correct!, you won the bouronvita gift hampper")
    elif (number - user_input) in (1, -1):
        print ("you are close")
    else:
        print ("Better Luck Next Time")