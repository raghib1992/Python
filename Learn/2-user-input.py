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


myfile = open('./Learn/file.txt')
print(myfile.seek(0))
print(myfile.read())

print(myfile.read())  #bo putput beacuse curse start from where it was left before and it was in the last word


print(myfile.seek(0))
print(myfile.read())


print(myfile.seek(0))
print(myfile.readlines())


myfile.close()


with open("./Learn/file.txt","r") as my_new_file:
    context = my_new_file.read()
    print(context)