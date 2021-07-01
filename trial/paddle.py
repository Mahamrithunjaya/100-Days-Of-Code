from turtle import Turtle


class Paddle(Turtle):
    # Create right paddle object
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setx(position)
        self.moving_up = False
        self.moving_down = False

    # The unused "event" parameter is used by the "s.getcanvas().bind("<Up>", paddle.move_up)" command in main.
    def move_up_true(self, event):
        self.moving_up = True

    def move_up_false(self, event):
        self.moving_up = False

    def move_down_true(self, event):
        self.moving_down = True

    def move_down_false(self, event):
        self.moving_down = False

    def move_up(self, paddle_y_pos):
        if self.moving_up and (paddle_y_pos < 300):
            new_y = self.ycor() + 10
            self.sety(new_y)

    def move_down(self, paddle_y_pos):
        if self.moving_down and (-300 < paddle_y_pos):
            new_y = self.ycor() - 10
            self.sety(new_y)