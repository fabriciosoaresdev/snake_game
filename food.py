from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__(shape='circle')

        self.speed('fastest')

        self.color('blue')

        self.penup()
        
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

        self.refresh()
    
    def refresh(self):
        self.goto(x = randint(-270, 270), y = randint(-270, 270))