from turtle import Turtle
import random

FOOD_COLOR = ["red", "springgreen", "gold"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_y = random.randint(-550, 550)
        random_x = random.randint(-550, 550)
        self.goto(random_x, random_y)
        random_color = random.randint(0, 2)
        self.color(FOOD_COLOR[random_color])
