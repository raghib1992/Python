from turtle import Turtle

MOVE_DISTANCE = 20
X_COORD = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for index in X_COORD:
          self.add_snake(index)  

    def add_snake(self,index):
        segment = Turtle(shape='square')
        segment.color('white')
        segment.penup()
        segment.goto(index)
        self.snakes.append(segment)
    
    def extend_snake(self):
        self.add_snake(self.snakes[-1].position())
    
    def move(self):
        for index in range(len(self.snakes)-1, 0, -1):
            # position = self.snakes[index-1].pos()
            new_x = self.snakes[index -1].xcor()
            new_y = self.snakes[index -1].ycor()
            self.snakes[index].goto(new_x,new_y)
        self.snakes[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.snakes[0].seth(90)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.snakes[0].seth(180)
    
    def down(self):
        if self.head.heading() != UP:
            self.snakes[0].seth(270)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.snakes[0].seth(0)
