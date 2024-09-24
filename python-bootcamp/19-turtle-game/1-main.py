# Project to work turtle to move forward when space key press

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    return tim.fd(100)


screen.listen()
screen.onkey(key='space',fun=move_forward)

screen.exitonclick()