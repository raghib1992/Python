from turtle import Turtle, Screen
import random
import turtle

all_turtle = []
color = ["red","green","blue","yellow","purple","orange"]
color_index = 0
x = -290
y = -100
race = False

screen = Screen()
screen.screensize(canvwidth=500, canvheight=400)
user_bet = screen.textinput(title="Make you bet", prompt="Who will win the race? Enter a colour")

# tim = Turtle(shape='turtle')



for index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color[index])
    new_turtle.penup()
    new_turtle.goto(x,y)
    y += 40
    all_turtle.append(new_turtle)


if user_bet in color:
    race = True

while race:
    for t in all_turtle:
        if t.xcor() >= 280:
            winner_color = t.pencolor()
            race = False
        distance_cover = random.randint(0,10)
        t.fd(distance_cover)  
if user_bet == winner_color:
    print("You won the match")
else:
    print(f"You lose the match\nWinner is {winner_color} turtle")
        
               
#     race = False
        
screen.exitonclick()