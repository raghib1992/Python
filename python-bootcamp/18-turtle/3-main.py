from turtle import Turtle, Screen
from random import choice
# Object
ton = Turtle()
tim = Screen()

# Variable
turtle_color = ["deep pink", "dark red", "lime", "cyan", "blue", "yellow", "medium purple"]
direction    = [ton.left(90), ton.right(90)]
angle = [90,180,270, 360]

# Code
for _ in range(200):
    ton.pensize(10)
    ton.color(choice(turtle_color))
    ton.speed("fastest")
    ton.forward(30)
    ton.setheading(choice(angle))
    

    


tim.exitonclick()