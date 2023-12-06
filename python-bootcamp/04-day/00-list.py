l = ["Nadim", "Rashid", "Shaheen"]
print(l)
#['Nadim', 'Rashid', 'Shaheen']
print(l[0])
# Nadim
print(l[-2])
# Rashid

l[0]="Raghib"
print(l)
#['Raghib', 'Rashid', 'Shaheen']

l.append("Uzma")
print(l)
#['Raghib', 'Rashid', 'Shaheen', 'Uzma']

l.remove("Raghib")
print(l)
#['Rashid', 'Shaheen', 'Uzma']

print(l.pop())
#Uzma
print(l)
#['Rashid', 'Shaheen']

l.extend(["uzma", "raghib"])
print(l)
#['Rashid', 'Shaheen', 'Uzma', 'Raghib']

l.pop(2)
print(l)
# ['Rashid', 'Shaheen', 'Raghib']
#*******

l = ["Raghib", True, 30]
print(l)
# ['Raghib', True, 30]

### List concatenate
Girl = ["Uzma", "Nilufar", "Neshat", "Shaheen"]
Boy = ["Rashid", "Raghib"]
print(f"Name of all brother and sisters are {Girl + Boy}")
# Name of all brother and sisters are ['Uzma', 'Nilufar', 'Neshat', 'Shaheen', 'Rashid', 'Raghib']
family = [Girl, Boy]
print(family)

a = [3,5]
b = [2,4]
print(a+b)
# [3, 5, 2, 4]

# Sort - sort in alphabetical order
name = ['uzma', 'nilu', 'raghib', 'rashid', 'neshat', 'shaheen', 'bushra', 'ilma', 'inaya', 'afsa', 'umar', 'abraaz']
print(name)
name.sort()
print(name)


# add list to list
l = [1,2,3,4]