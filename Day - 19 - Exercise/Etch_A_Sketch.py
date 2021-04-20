from turtle import Turtle, Screen

beam = Turtle()
my_screen = Screen()


def move_forwards():
    beam.forward(10)


def move_backwards():
    beam.backward(10)


def move_counter_clockwise():
    # beam.left(10)
    new_heading = beam.heading() + 10
    beam.setheading(new_heading)


def move_clockwise():
    # beam.right(10)
    new_heading = beam.heading() - 10
    beam.setheading(new_heading)


def clear_screen():
    # beam.clear()
    # beam.reset()
    beam.clear()
    beam.penup()
    beam.home()
    beam.pendown()


my_screen.listen()

my_screen.onkey(key="w", fun=move_forwards)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="a", fun=move_counter_clockwise)
my_screen.onkey(key="d", fun=move_clockwise)
my_screen.onkey(key="c", fun=clear_screen)

my_screen.exitonclick()
