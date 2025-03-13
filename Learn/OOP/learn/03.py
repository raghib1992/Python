# The string representation of an object WITHOUT the __str__() function:


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"My name is {self.name} and I am {self.age} years old"


p1=Person("Raghib", 31)

print(p1)