from turtle import Turtle

MOVE_DISTANCE = 10
STARTING_POSITION = -280
FINISH_LINE = 280

class Tim(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('turquoise')
        self.penup()
        self.reset_position()
        self.seth(90)
        
    def move(self):
        self.fd(20)
        
    def reset_position(self):
        self.goto(0,STARTING_POSITION)

    def final_position(self):
        if self.ycor() == FINISH_LINE:
            return True
        else:
            return False
    
