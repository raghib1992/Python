family = {"Raghib":29, "Rashid":26, "Shaheen":21}

family["Ilma"]=3

print(family["Raghib"])

for fa in family:
    print(f"{fa}:{family[fa]}")
print(fa)
for fa, age in family.items():
    print(f"{fa}: {age}")


home = [
    {"name": "Raghib", "age": 29},
    {"name": "Rashid", "age": 26},
    {"name": "Shaheen", "age": 21},
]

print(home[1])


student = {"Ram": 95, "Sita":99, "Goyal":97}

if "Ram" in student:
    print(f"Ram: {student['Ram']}")
else:
    print("Ram is not the student of the class")

attendance = student.values()
print(f"The average attendance of the whole class {sum(attendance)/len(attendance)}")