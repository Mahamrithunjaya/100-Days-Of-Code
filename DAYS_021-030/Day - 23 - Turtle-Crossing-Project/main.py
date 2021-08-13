import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.bgpic("road.jpg")
my_screen.tracer(0)
my_screen.colormode(255)
my_screen.setup(width=800, height=600)
my_screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()
my_screen.onkey(fun=player.go_up, key="Up")


def death_pointer():
    point = Turtle()
    point.hideturtle()
    point.pencolor("red")
    point.penup()
    point.pensize(5)
    my_screen.bgcolor("red")
    point.goto(player.xcor(), player.ycor() - 20)
    player.stamp()
    player.hideturtle()
    point.pendown()
    for a in range(4):
        point.circle(30)
        my_screen.update()
        time.sleep(0.5)
        point.clear()
        my_screen.update()
        time.sleep(0.5)
    point.circle(30)
    my_screen.update()


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    my_screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect Collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            death_pointer()
            scoreboard.game_over()

    # Detect successful crossing along Y-axis
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start()
        car_manager.level_up_speed()

    # Removes the blocks from -ve X axis
    car_manager.remove_cars()


my_screen.exitonclick()
