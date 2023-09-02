# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of someone's weight taking into account their heigh


weight = int(input("Enter your Weight in kg: \n"))
height = float(input("Enter your height in cm: \n"))
# Convert cm to meter
height_new = height/100

bmi = str(int(weight/(height_new**2)))
print("Your BMI is " + bmi)