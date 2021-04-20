from turtle import Turtle


class Borders(Turtle):

    def __init__(self):
        super().__init__()
        self.pos = self.position
        self.head = self.heading()
        self.create_borders()

    @staticmethod
    def create_border(position, heading, forward):
        border = Turtle()
        border.color("orange")
        border.ht()
        border.penup()
        border.pensize(width=2)
        border.goto(position)
        border.pendown()
        border.setheading(heading)
        border.forward(forward)

    def create_borders(self):
        # Right Border
        self.create_border((320, 320), 270, 640)
        # Left Border
        self.create_border((-320, 320), 270, 640)
        # UP Border
        self.create_border((-320, 320), 0, 640)
        # Down Border
        self.create_border((-320, -320), 0, 640)
