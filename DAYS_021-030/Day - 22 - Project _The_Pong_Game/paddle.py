from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.pos = position
        self.direction = "Up"
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.pos)

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), 250)

    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), -250)

    def move_auto(self):
        if self.direction == "Up":
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)
        elif self.direction == "Down":
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)
