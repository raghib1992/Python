from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Setup screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Pong')
screen.tracer(0)

# Create Paddle
r_paddle = Paddle(380)
l_paddle = Paddle(-380)

# move paddle from input
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Create Ball
ball = Ball()

r_score = Scoreboard((60,250))
l_score = Scoreboard((-60,250))

game_on = True
while game_on:
    time.sleep(0.07)
    screen.update()
    ball.move()
    
    # Bouncing from top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncing()
        
    # hit r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit_paddle()
    
    #  r_paddle missed
    if ball.xcor() > 380:
        ball.reset_ball()
        l_score.increase_score()

    #  l_paddle missed
    if ball.xcor() < -380:
        ball.reset_ball()
        r_score.increase_score()


screen.exitonclick()
