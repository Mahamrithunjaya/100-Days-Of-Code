from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("brown1")
        self.penup()
        self.shapesize(1)
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    # Here the ball is moving upwards so values of (x,y) are in +ve
    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    # Here we reverse the direction of the ball y-axis by multiplying it by -1
    def bounce_y(self):
        self.y_move *= -1

    # Here we reverse the direction of the ball x-axis by multiplying it by -1
    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
