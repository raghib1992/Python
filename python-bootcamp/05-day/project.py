#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print('')
print("Your password is generating")
print("Please wait")
print('')
password = []
for l in range(1,nr_letters+1):
    get_index = random.randrange(len(letters))
    sub_passowrd = (letters[get_index])
    # password += sub_passowrd
    password.append(sub_passowrd)

for s in range(1,nr_symbols+1):
    get_index = random.randrange(len(symbols))
    sub_passowrd = (symbols[get_index])
    # password += sub_passowrd
    password.append(sub_passowrd)

for s in range(1,nr_numbers+1):
    get_index = random.randrange(len(numbers))
    sub_passowrd = (numbers[get_index])
    # password += sub_passowrd
    password.append(sub_passowrd)


print(password)
(random.shuffle(password))
print(password)
print (''.join(password))
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P