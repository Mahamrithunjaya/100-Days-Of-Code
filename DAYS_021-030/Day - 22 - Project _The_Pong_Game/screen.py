from turtle import Turtle


class Board:

    def __init__(self):
        self.board = Turtle()
        self.board.hideturtle()
        self.board.color("green")
        self.board.penup()
        self.board.goto(-360, -300)
        self.board.pendown()
        self.board.forward(720)
        self.board.setheading(90)
        self.board.forward(600)
        self.board.setheading(180)
        self.board.forward(720)
        self.board.setheading(270)
        self.board.forward(600)
        self.board.setheading(90)
        self.board.goto(0, -300)
        self.board.forward(600)
