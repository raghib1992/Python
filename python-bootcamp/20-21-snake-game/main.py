from turtle import Turtle, Screen
import time
from snake import Snake
import random
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

# Create snake using Snake class
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Create Food
food = Food()

# Create Scoreboard
scoreboard = Scoreboard()

game_on = True

while game_on:
    screen.update()
    time.sleep(0.2)
    # Move snake
    snake.move()
    
    # snake hit the food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend_snake()
        food.refresh()

    # Snake hit wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_on = False

    # Collision with body
    # for segemnt in snake.snakes:
    #     if snake.head == segemnt:
    #         pass
    #     elif snake.head.distance(segemnt) < 10:
    #         scoreboard.game_over()
    #         game_on = False

    # above same with slice method
    for segment in snake.snakes[1::]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False





screen.exitonclick()