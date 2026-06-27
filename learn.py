class Car():

    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed

    def honk(self):
        return self.brand + " goes beep Beep"
    

car1 = Car("Bugati", "Black", 315)
car2 = Car("Lamborgini", "Yellow", 200)


print(car1.honk())