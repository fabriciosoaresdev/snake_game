from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

run_game = True
snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while run_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()   
        score.scoring()
        snake.extend()
    
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        
        run_game = False

        score.game_over()
    
    for piece_body in snake.body[1:]:
        if snake.head.distance(piece_body) < 10:
            run_game = False
            score.game_over()

screen.exitonclick()