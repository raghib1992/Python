# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
scores = 0 
for score in student_scores:
    if int(score) > scores:
        scores = int(score)
print(scores)