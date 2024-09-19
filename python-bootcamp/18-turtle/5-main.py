import turtle as t
import random


tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

angle = 0

while angle < 360:
    tim.shape("turtle")
    tim.color(random_color())
    tim.speed("fast")
    tim.circle(100)
    tim.left(10)
    angle += 10
