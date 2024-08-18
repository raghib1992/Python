#Write a program that works out whether if a given number is an odd or even number.

# Ask for a number
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("Input number is Even")
else:
    print("Number is odd")