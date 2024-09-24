from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    return tim.fd(10)

def move_backward():
    return tim.bk(10)

def clockwise():
    return tim.right(10)

def counter_clockwise():
    return tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    
screen.listen()
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='d',fun=clockwise)
screen.onkey(key='a',fun=counter_clockwise)
screen.onkey(key='c',fun=clear)
screen.exitonclick()