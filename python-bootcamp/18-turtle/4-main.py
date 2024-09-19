from turtle import Turtle, Screen, colormode
import random

# Object
ton = Turtle()
tim = Screen()
colormode(255)


# Variable
angle = [90,180,270, 360]

# color 
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

# Code
for _ in range(200):
    ton.pensize(10)
    ton.color(random_color())
    ton.speed("fastest")
    ton.forward(30)
    ton.setheading(random.choice(angle))
    

    


tim.exitonclick()