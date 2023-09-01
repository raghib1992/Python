import math

# Calculate how much paint required to paint a wall
# 1 can of paint can cover 5 square meter
# Ask for wall size


def number_of_can(height,weidth):
    can = math.ceil((height*weidth)/5)
    print(f"Number of can required to paint a wall {can}")



input1 = int(input("What is the height of the wall: "))
input2 = int(input("What is the width of the wall: "))

number_of_can(height=input1, weidth=input2)