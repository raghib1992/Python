# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 

# Then check for the number of times the letters in the word LOVE occurs. 

# Then combine these numbers to make a 2 digit number.
name1 = input("first person name? ")
name2 = input("second person name? ")

t = ((name1 + name2).lower()).count("t")
r = ((name1 + name2).lower()).count("r")
u = ((name1 + name2).lower()).count("u")
e = ((name1 + name2).lower()).count("e")


l = ((name1 + name2).lower()).count("l")
o = ((name1 + name2).lower()).count("o")
v = ((name1 + name2).lower()).count("v")

true = t + r + u + e
love = l + o + v + e

print('')
num = int(str(true) + str(love))


if num < 10 or num > 90:
    print(f"Your score is **{num}**, you go together like coke and mentos.")
elif num >= 40 and num < 50:
    print(f"Your score is **{num}**, you are alright together.")
else:
    print(f"Your score is **{num}**.")