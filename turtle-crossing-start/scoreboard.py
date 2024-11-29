from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level_number = 1
        self.level()

    def level(self):
        self.clear()
        self.goto(x=-290, y=260)
        self.write(f"Level: {self.level_number}", align="left", font=FONT)

    def level_up(self):
        self.level_number += 1
        self.level()

    def game_over(self):
        self.goto(x=-0, y=0)
        self.write("Game Over!!", align="center", font=FONT)
