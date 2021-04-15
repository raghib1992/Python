numbers = [1,2,3,4,5,6,7,8,9]
double =[] # list of variable in double is 2 times of numbers' list

for num in numbers:   # iteration
    double.append(num * 2)  # append

print(double)

x = [1,2,3]
y = [z*2 for z in x]
print(y)


friends = ["Ziya", "Sana", "Farhan", "Soaib", "Rashid", "Shaheen"]
start_S = []

for friend in friends:
    if friend.startswith("S"):
        start_S.append(friend)

print(start_S)

friends = ["Ziya", "Sana", "Farhan", "Soaib", "Rashid", "Shaheen", "Raghib"]
start_S = [friend for friend in friends if friend.startswith("R")]

print(start_S)

print("friends: ", id(friends), "start_S: ", id(start_S))