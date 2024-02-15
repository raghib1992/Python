class Person:
    # Create name attribute 
    def __init__(self, name):
        self.name = name
    
    # Create talk method
    def talk(self):
        print(f"Hi, I am {self.name}")

raghi = Person("Raghib")
print(raghi.name)
raghi.name = "uzma"
raghi.talk()