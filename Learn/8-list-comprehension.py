numbers = [1,2,3]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print (doubled)

# list comprehension
numbers = [1,2,3]
doubled = [num *2 for num in numbers]

############
friends = ['Zaman', 'Shreyanka', 'Sanober', 'saba', 'Shagufta']
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)
print(starts_s)

friends = ['Zaman', 'Shreyanka', 'Sanober', 'saba', 'Israr']
starts_s = [friend for friend in friends if friend.startswith("S")]

print(starts_s)