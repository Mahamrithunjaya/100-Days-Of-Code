from turtle import Turtle

SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Courier", 60, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-160, 290)
        self.write(self.l_score, align=SCORE_ALIGNMENT, font=SCORE_FONT)
        self.goto(160, 290)
        self.write(self.r_score, align=SCORE_ALIGNMENT, font=SCORE_FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("DarkRed")
        self.write(arg="GAME OVER !!!", align=SCORE_ALIGNMENT, font=("Courier", 60, "bold"))
        if self.l_score == 20:
            self.goto(-300, 150)
            self.color("orange")
            self.write("Left Side Won !!!", font=("Courier", 15, "bold"))
        elif self.r_score == 20:
            self.goto(80, 150)
            self.color("orange")
            self.write("Right side Won !!!", font=("Courier", 15, "bold"))
