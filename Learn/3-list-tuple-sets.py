# List
l = ["Nadim", "Rashid", "Shaheen"]
print(l[0])

# list are mutable
l[0] ="bhaijaan"
print(l)

l.append('Uzma')
print(l)

l.remove('bhaijaan')
print(l)
## pop up last element from list
l = ["Nadim", "Rashid", "Shaheen"]
l.append("Sanober")
print(l)
love = l.pop()
print(l)
print(f"My love is {love}")

vowel = ["a", "e", "i", "s", "o", "u"]
print(vowel)
consonent = vowel.pop(3)
print(vowel)


l = ["Raghib", "age", 30]
print(l)

### List concatenate
Girl = ["Uzma", "Nilufar", "Neshat", "Shaheen"]
Boy = ["Rashid", "Raghib"]

print(f"Name of all brother and sisters are {Girl + Boy}")

# Sort - sort in alphabetical order
name = ['uzma', 'nilu', 'raghib', 'rashid', 'neshat', 'shaheen', 'bushra', 'ilma', 'inaya', 'afsa', 'umar', 'abraaz']
print(name)
name.sort()
print(name)


#Tuple (immutable)
# tuple , tuple can't be modified
t = ('Jawed', 'Israr', 'Zaman', 'Zaman')
print(t[2])
print(t.count('Zaman'))
print(t.index('Israr'))

# Set
# set set not allowed order
car = {"BMW", "Merceedes", "Jaguar"}
print(car)

# MOdify sets
car.add("Verna")
print(car)

num = [1,1,1,1,1,1,3,3,3,3,3,2,2,2,2,5,5,5,5,5]
print(set(num))

# sets
friends = {'Pappu', 'Zaman', 'Waquar', 'Murad', 'Irshad', 'Israr', 'Jitender'}
Kolkata = {'Pappu', 'Zaman'}
Village_friend = friends.difference(Kolkata)

Delhi = {'Israr', 'Jitender'}

city_friends = Kolkata.union(Delhi)
print(Village_friend)

common_frinds = Village_friend.intersection(Delhi)
