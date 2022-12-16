from turtle import Turtle
FONT = ("Franklin Gothic Medium", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 1

    def increase_score(self):
        self.level += 1
        self.clear()
        self.scoreboard()
    def scoreboard(self):
        self.write(f"Level: {self.level}", font=FONT)
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center",font=FONT)