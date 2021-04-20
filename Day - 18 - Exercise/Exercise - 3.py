from turtle import Turtle, Screen
import random

nibbi_the_turtle = Turtle()
nibbi_the_turtle.shape("classic")
# tim.color("DodgerBlue3")

colors = ["firebrick", "LimeGreen", "blue4", "cyan2", "chocolate", "gold1", "DarkMagenta", "DeepPink2"]
color_list = []


def generate_color():
    random_color = random.choice(colors)
    while random_color in color_list:
        random_color = random.choice(colors)
    color_list.append(random_color)

    return nibbi_the_turtle.pencolor(random_color)


def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        nibbi_the_turtle.forward(100)
        nibbi_the_turtle.right(angle)


for shape_side_n in range(3, 11):
    generate_color()
    draw_shape(shape_side_n)


my_screen = Screen()
my_screen.exitonclick()
