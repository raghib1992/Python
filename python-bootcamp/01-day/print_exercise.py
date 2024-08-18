# Print function
print("Hi Uzma")
print("Hello" + " " + "World")
print("Hi Raghib today is Tuesday\nHope you plan to go to office tomorrow")

#Input
print(input("A Promt for user: "))
print("hello " + input("What is your name? "))
print("To know Lenght of your Name")
print("lenght of your name is:  " + str(len(input("What is your name? ").replace(" ","")))) # only concatenate str (not "int") to str


name = input("What is your name: ")
length = len(name) - name.count(" ")

print(f"Number od letter in your name is {length}")