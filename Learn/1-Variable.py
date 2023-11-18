# Integer
x = 15

# Float
y = 9.21
result = 100/777
print(f"The result was {result}")
# "{value:width.precison f}"
print(f"The result was {result:1.3f}")
# priint function and what it will print in the bracket
print(y)

# String
name = "Raghib"
print (name * 2)

name = 'Shaheen'
title = 'akhtar'
print (name + title)
print (name + " " + title)

name = 'Uzma'
title = 'Akhtar'
greeting = f'Hello, {title}'
print(f"Hello, {name}")
print(greeting)

name = "Uzma"
print(f"Hello, {name}")
print("Hi {}, How are you?".format(name))
print (greeting)

a="uzma"
b="nilu"
c="neshat"
d="shaheen"
print("Hi sisters {}, {}, {} and {}".format(a,b,c,d))

print("Hi {b} {i} {ii} {a}".format(a='Afsa',ii='Inaya',i="Ilma",b="Bushra"))

# Template
name = "Nadim"
greeting = "Hello {}, How are you?"
# format function
with_name = greeting.format(name)
with_name = greeting.format("Raghib")
print (with_name)

head, *fail = [1,2,3,4,5]
print (head, fail)

sir, *pao = [1,2,3,4,5,6]
print(sir, pao)

#***************************
# Indexing 
Greet = "Hello Raghib"
print(Greet[0])
print(Greet[10])
print(Greet[-2])
# slicing
alphabet = "ABCDEFGHIJKLMNOPQRSTUVMXYZ"
print(alphabet[6])
print(alphabet[:6])  # don include index posiiton
### required ghi
print(alphabet[6:9])
print(alphabet[::2])
print(alphabet[::-1])

# String are Immutability , i.e you can't change the string example below
# Name = "Sarma"
# Name[0] = "K"
# print(Name)  

## string concatenation.
Name = "Raghib"
last_letter = Name[1:]
New_Name = "S" + last_letter
print(Name)
print(New_Name)


statement = "Hyderabad is a very beautiful city and people of Hyderabad is very polite"
print(statement.split())


# Trunc


import math
float = 12.86785
print("The value of number is: ",end="")
print (math.trunc(float))