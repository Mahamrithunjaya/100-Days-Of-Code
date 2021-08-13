from turtle import Turtle, Screen

nibbi_the_turtle = Turtle()

nibbi_the_turtle.shape("turtle")
nibbi_the_turtle.color("DodgerBlue3")

for _ in range(4):
    nibbi_the_turtle.forward(100)
    nibbi_the_turtle.right(90)

turtle_screen = Screen()
turtle_screen.exitonclick()
