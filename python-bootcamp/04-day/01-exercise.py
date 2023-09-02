# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function
import random

# nam = input("Give the list of name separated by \",\": ")
# name = nam.split(",")
# print(name)
name = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# print(random.choice(name))

num = random.randint(0,(len(name)-1))
print(num)
print(name[num])