from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setheading(45)
        self.speed(5)
        self.ball_accel = 1.05

    def bounce_border(self):
        self.setheading(360 - self.heading())

    def reset_position(self):
        self.goto(0, 0)
        self.setheading(180 - self.heading())