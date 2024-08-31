class Dog:
    # Attributes: A data for the dog object
    breed = ''
    age   = 0

    # Method (Function) of Dog bark
    def bark(self):
        print('Wooof!!!')


# Create an object from Dog Class
my_dog = Dog()
my_dog.breed = "Labrador"
my_dog.age = 12


# Call the bark method of the object (dog)
my_dog.bark()