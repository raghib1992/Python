# Class inheritance
from turtle import Turtle
import time
import random

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.color('chartreuse')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed('fastest')
        self.refresh()
        
    def refresh(self):
        x_pos = random.randint(-290,290)
        y_pos = random.randint(-290,290)
        self.goto(x_pos,y_pos)
