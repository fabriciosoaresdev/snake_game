from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')

        self.speed('fastest')
        
        self.score = 0

        self.penup()

        self.goto(x = 0, y = 280)

        self.refresh_score()

    def refresh_score(self):

        self.write(f'Score: {self.score}', False, 'center', ('Arial', 14, 'normal'))
        
        self.hideturtle()
    
    def scoring(self):
        self.clear()

        self.score += 1

        self.write(f'Score: {self.score}', False, 'center', ('Arial', 14, 'normal'))
        
        self.hideturtle()

    def game_over(self):
        super().__init__()

        self.color('white')

        self.speed('fastest')

        self.hideturtle()

        self.write(f'GAME OVER', False, 'center', ('Arial', 14, 'normal'))
        

