from turtle import Turtle

FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        
    def level_score(self):
        self.color('white')
        self.penup()
        self.goto(-240,260)
        self.clear()
        self.write(f"level: {self.score}", align='center', font=FONT)
        self.hideturtle()
        
    def game_over(self):
        self.color('white')
        self.penup()
        self.goto(0,0)
        self.clear()
        self.write(f"Game Over", align='center', font=FONT)
        self.hideturtle()
    
    def level_increase(self):
        self.score += 1