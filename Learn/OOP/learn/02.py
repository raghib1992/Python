# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

p1 = Person("Raghib",31)
p2 = Person("Uzma", 24)

print(p1.name , p1.age)

print(p2.name)