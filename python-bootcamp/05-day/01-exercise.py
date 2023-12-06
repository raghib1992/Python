# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split(",")
print(student_heights)

# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

for h in student_heights:
    add = 0
    add += int(h)

print(add)
average_height = add/len(student_heights)
print(average_height)
#Write your code below this row 👇

