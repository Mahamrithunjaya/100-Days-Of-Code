from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Roboto", 24, "normal")
STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVING_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head_mod()
        self.activate = False

    # Creates Snakes
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("orange")
        new_segment.shapesize(0.5, 0.5)
        new_segment.goto(position)
        self.segments.append(new_segment)

    # It first clears all the segments of the snake, then creates another three-segment snake in the starting position
    # and after that it set the self.head as the zeroth element from that list of segments
    # Basically we're doing everything that in init() because we're going to initialize
    # the snake again, back at the center
    def reset_snake(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head_mod()

    # Adding new segment to the end of the list
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def head_mod(self):
        self.head.color("cyan")
        self.head.shape("circle")
        self.head.shapesize(0.6, 0.8)

    # Moves Snakes
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
