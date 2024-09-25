from turtle import Turtle, Screen
from paddle import Paddle


# Setup screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Pong')
screen.tracer(0)

# Create Paddle
l_paddle = Paddle(380)
r_paddle = Paddle(-380)

# move paddle from input
screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update()

 




screen.exitonclick()
