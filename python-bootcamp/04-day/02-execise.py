# Hide the treasure in any white block position.

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

# Enter 2 digit input. FIrst digit input for row and second dit for coloumn. value of both digit should be 1,2 and 3.
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# #Write your code below this row 👇
vertical = int(position[1]) -1
horizontal = int(position[0]) - 1
map[vertical][horizontal] = "x"

# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

