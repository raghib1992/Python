def add(*args):
    plus = 0
    for n in args:
        plus += n
    print(plus)
    
    
add(1,2,3,4,5,6,7)


def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
   
    
calculate(2, add= 5, multiply= 3)


class Car:
    
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="ford",model="mustang")
print(my_car.make)

# How to use get instead of ks
class Bus:
    
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_bus = Bus(make="Ford")
print(my_car.model)