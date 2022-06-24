class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return (f"Hello, {self.name} you are {self.age} years old")

    def __repr__(self):
        return f"<Person {self.name}, {self.age}>"

bob = Person("bob", 32)

print(bob)