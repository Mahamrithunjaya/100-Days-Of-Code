from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=800, height=600)
user_bet = my_screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "DarkBlue", "purple", "SpringGreen", "DarkTurquoise"]
all_turtles = []
is_race_on = False

y_axis = -220
for turtle_index in range(0, 8):
    new_turtle = Turtle(shape="turtle")
    # The default size of a Turtle object is 20 pixels.
    # Sets the turtle's width to 40px and height to 40px and width of the Turtle's outline to 1
    new_turtle.shapesize(2, 2, 1)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-380, y=y_axis)
    y_axis += 65
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        # 360 is 400 - half the width of the turtle.
        if turtle.xcor() > 360:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f" You've won! The {winning_color} turtle is the winner! ")
            else:
                print(f" You've lost! The {winning_color} turtle is the winner! ")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


my_screen.exitonclick()
