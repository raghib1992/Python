# Integer
x = 15

# Float
y = 9.21

# priint function and what it will print in the bracket
print(y)

# String
name = "Raghib"
print (name * 2)

name = 'Shaheen'
title = 'akhtar'
print (name + title)

name = 'Yashmin'
greeting = f'Hello, {name}'
print(f"Hello, {name}")

name = "Rashid"
print(f"Hello, {name}")
print (greeting)

# Template
name = "Nadim"
greeting = "Hello {}, How are you?"
# format function
with_name = greeting.format(name)
with_name = greeting.format("Raghib")
print (with_name)


head, *fail = [1,2,3,4,5]
print (head, fail)