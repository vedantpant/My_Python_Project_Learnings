from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", 'r') as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 310)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score : {self.score}  High Score : {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    '''def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!!", align=ALIGNMENT, font=FONT)'''

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", 'w') as data:
                self.write(f"score : {self.score}  High Score : {data.write(str(self.highscore))}", align=ALIGNMENT,
                           font=FONT)
        self.score = 0
        self.update_scoreboard()
