from turtle import Turtle
import random

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'gold', 'DarkGreen',
          'DarkSalmon', 'LightCyan3', 'maroon1']


class Food(Turtle):

    # All of this is going to happen as soon as we create a new food object from the food class.
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Resizing the shape to 10px X 10px
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        self.color(random.choice(COLORS))
        rand_x = random.choice(range(-300, 300, 20))
        rand_y = random.choice(range(-300, 300, 20))
        self.goto(rand_x, rand_y)
