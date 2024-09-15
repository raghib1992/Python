from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")

for _ in range(4):
    tim.forward(100)
    tim.right(90)

tom = Turtle()
tom.shape("turtle")
tom.color("green")
tom.circle(50)

screen = Screen()
screen.exitonclick()