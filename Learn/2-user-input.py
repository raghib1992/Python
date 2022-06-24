# name = input("Enter your name: ")

#Convert Fahrenheit into Degree
Fahrenheit = input("Fahrenheit Value: ")
f = float(Fahrenheit)
degree = (f-32)*(5/9)

print(f"{f} Fahrenheit is equal to {degree:.2f} degree")


# Convert Years into Months

Years = int(input("Enter the number of years: "))
months = Years * 12
print(f"{Years} years is equal to {months} months")