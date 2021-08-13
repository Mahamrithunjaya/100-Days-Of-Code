import turtle
import random

tim = turtle.Turtle()
my_screen = turtle.Screen()
tim.shape("classic")
turtle.colormode(255)
my_screen.setup(width=800, height=600)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(500):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


my_screen.exitonclick()
