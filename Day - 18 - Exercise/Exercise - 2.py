from turtle import Turtle, Screen

nibbi_the_turtle = Turtle()
nibbi_the_turtle.shape("turtle")
nibbi_the_turtle.color("DodgerBlue3")

for _ in range(20):
    nibbi_the_turtle.pencolor("gold1")
    nibbi_the_turtle.forward(10)
    nibbi_the_turtle.penup()
    nibbi_the_turtle.forward(10)
    nibbi_the_turtle.pendown()

my_screen = Screen()
my_screen.exitonclick()
