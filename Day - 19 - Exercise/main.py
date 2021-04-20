from turtle import Turtle, Screen

beam = Turtle()
my_screen = Screen()


def move_forwards():
    beam.forward(20)


my_screen.listen()
my_screen.onkey(key="space", fun=move_forwards)
my_screen.exitonclick()
