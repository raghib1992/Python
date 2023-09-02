#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# Welcome to tip calculator
bill=input("What was the total bill?\n$")
tip = input("What percent tip would you like to give? 10,12,or 15:\n")
person = input("How many person to split the bills? ")

total_amount = float(float(bill) * (1 + int(tip)/100))
print(total_amount)
per_person = round(total_amount/int(person),2)

per_person = "{:.2f}".format(total_amount)
print(per_person)
print(f"Each Person should pay: ${per_person}")