# List
l = ["Nadim", "Rashid", "Shaheen"]
print(l[0])

# modify list
l[0] ="bhaijaan"
print(l)

l.append('Uzma')
print(l)

l.remove('bhaijaan')
print(l)

#Tuple
# tuple , tuple can't be modified
t = ('Jawed', 'Israr', 'Zaman')
print(t[2])


# Set
# set set not allowed order
s = {"BMW", "Merceedes", "Jaguar"}
print(s)

# MOdify sets
s.add("Jitender")
print(s)

# sets
friends = {'Pappu', 'Zaman', 'Waquar', 'Murad', 'Irshad', 'Israr', 'Jitender'}
Kolkata = {'Pappu', 'Zaman'}
Village_friend = friends.difference(Kolkata)

Delhi = {'Israr', 'Jitender'}

city_friends = Kolkata.union(Delhi)
print(Village_friend)

common_frinds = Village_friend.intersection(Delhi)