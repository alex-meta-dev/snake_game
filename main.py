# Snake mini game
# Alexandru Meta
# 13 March 2023

from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1200, height=1200)
screen.bgcolor("black")
screen.title("Snakey")
screen.tracer(0)

time.sleep(0.1)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        if food.pencolor() == "gold":
            scoreboard.increase_score(3)
        else:
            scoreboard.increase_score(1)
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 590 or snake.head.xcor() < -590 or snake.head.ycor() > 590 or snake.head.ycor() < -590:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
