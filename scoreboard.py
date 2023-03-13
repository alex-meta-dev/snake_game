from turtle import Turtle
from playsound import playsound

ALIGNMENT = "center"
FONT = ("Courier", 28, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.message = "GAME OVER"
        self.score = 0
        self.goto(0, 560)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def increase_score(self, amount):
        self.score += amount
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:  {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        playsound("sounds/ES_Video Game Over - SFX Producer.mp3")
        self.clear()
        self.goto(0, 0)
        self.write(f"{self.message}", align=ALIGNMENT, font=("Courier", 80, "normal"))
        self.color("white")
        self.hideturtle()


