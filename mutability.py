# Liast are mutable


a = []
b = a

a.append(90)

print(id(a))
print(id(b))

b =[]

print(id(b))

# Integers are immutable
# Tuple are imutable