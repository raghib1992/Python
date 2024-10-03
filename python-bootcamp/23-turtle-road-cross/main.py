from turtle import Screen
from tim import Tim
from traffic import Traffic
import time
from scoreborad import Scoreboard


screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.listen()

timmy = Tim()
screen.onkey(timmy.move, "Up")
 
vehical = Traffic()
score = Scoreboard() 
score.level_score()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    vehical.create_cars()
    vehical.move_traffic()
    
    for car in vehical.all_cars:
        if timmy.distance(car) < 20:
            score.game_over()
            game_on = False

    if timmy.final_position():
        timmy.reset_position()
        vehical.level_up()
        score.level_increase()
        score.level_score()
        






screen.exitonclick()