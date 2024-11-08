from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self,postion):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(postion)
        self.write(f"{self.score}", align='center', font=("Arial", 36, "normal"))
        self.hideturtle()
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align='center', font=("Arial", 36, "normal"))
        self.hideturtle()
        