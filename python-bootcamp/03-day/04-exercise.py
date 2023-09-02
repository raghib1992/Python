# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

order = input("What size of pizza do you want? (Small, Medium or Large) \n")
pep = input("Do you want pepperoni? (Y or N) ")
cheese = input("Doyou wnt extra cheese? (Y or N) ")

if order == "Small":
    bill = 15
    if pep == "Y":
        bill += 2
elif order == "Medium":
    bill = 20
    if pep == "Y":
        bill += 3
elif order == "Large":
    bill = 25
    if pep == "Y":
        bill += 3
else:
    print("Invalid input")

if cheese == "Y":
    bill +=1
print(f"Your total amount is {bill}")
