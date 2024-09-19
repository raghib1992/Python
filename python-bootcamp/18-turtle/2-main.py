import turtle as t
import random

tac = t.Turtle()

# for _ in range(15):
#     tac.forward(10)
#     tac.penup()
#     tac.forward(10)
#     tac.pendown()

side = 3
turtle_color = ["deep pink", "dark red", "lime", "cyan", "blue", "yellow", "medium purple"]

while side <= 7:
    tac.shape("turtle")
    tac.color(random.choice(turtle_color))
    for _ in range(side):
        angle = 360/side
        tac.forward(100)
        tac.right(angle)
    side += 1

tit = t.Screen()
tit.exitonclick()