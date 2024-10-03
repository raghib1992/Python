from turtle import Turtle
import random

COLORS = ["red", "orange", "blue", "yellow", "green", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Traffic:

    def __init__(self) -> None:
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
   
    def create_cars(self):
        random_num = random.randint(1,4)
        if random_num == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-260,260)
            new_car.goto(270,random_y)
            self.all_cars.append(new_car)

    def move_traffic(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
