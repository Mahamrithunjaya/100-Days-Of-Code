import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()

color_list = [(223, 18, 244), (40, 94, 151), (183, 42, 74), (228, 207, 97), (211, 154, 85), (181, 169, 29),
              (140, 88, 58), (116, 177, 210), (203, 73, 123), (214, 128, 174), (232, 67, 46), (92, 101, 189),
              (146, 32, 62), (44, 166, 118), (50, 55, 95), (16, 155, 82), (117, 45, 34), (119, 217, 210),
              (33, 185, 197), (221, 174, 191), (127, 194, 176), (214, 204, 34), (176, 187, 216), (46, 52, 71),
              (156, 207, 219), (227, 176, 167), (41, 77, 81)]

number_of_dots = 100
tim.speed("fastest")
tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(350)
tim.setheading(0)

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


my_screen = turtle_module.Screen()
my_screen.exitonclick()
