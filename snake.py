from turtle import Turtle

POSITION = [(0,0), (-20,0), (-40,0)]

UP, DOWN, RIGHT, LEFT = 90, 270, 0, 180

DISTANCE = 20

class Snake():

    def __init__(self):

        self.body = []

        self.add()

        self.head = self.body[0]

    def add(self):
        for position in POSITION:
            self.add_piece(position)
        
    def add_piece(self, position):
            snake = Turtle(shape='square')

            snake.color('white')

            snake.penup()

            snake.goto(position)
        
            self.body.append(snake) 
    
    def extend(self):
        self.add_piece(self.body[-1].position())

    def move(self):
        for part_body in range(len(self.body) - 1, 0, -1):
            
            cor_x = self.body[part_body - 1].xcor()
            
            cor_y = self.body[part_body - 1].ycor()

            self.body[part_body].goto(x = cor_x, y = cor_y)

        self.head.forward(DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            self.head.setheading(DOWN)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        else:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            self.head.setheading(RIGHT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        else:
            self.head.setheading(LEFT)