from paddle import Paddle
from ball import Ball
from turtle import Screen
from scoreboard import ScoreBoard
from screen import Board
import time

my_screen = Screen()
my_screen.title("Welcome to the Pong Game - The Famous Arcade Game")
my_screen.bgcolor("black")
my_screen.setup(width=900, height=750)
my_screen.listen()
my_screen.tracer(0)

new_board = Board()

# Asking user to enter a choice of the game
user_choice = my_screen.textinput(title="Select Player      GAME-POINT = 20",
                                  prompt="Enter your choice ( SINGLEPLAYER / MULTIPLAYER )").lower()

r_paddle = Paddle((350, 0))
r_paddle.color("VioletRed")
l_paddle = Paddle((-350, 0))
l_paddle.color("yellow")

my_screen.onkeypress(fun=r_paddle.go_up, key="Up")
my_screen.onkeypress(fun=r_paddle.go_down, key="Down")
my_screen.onkeypress(fun=l_paddle.go_up, key="w")
my_screen.onkeypress(fun=l_paddle.go_down, key="s")

ball = Ball()
scoreboard = ScoreBoard()

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    my_screen.update()
    ball.move()

    # Checking the user's choice input
    if user_choice == "singleplayer":
        r_paddle.move_auto()
        # change direction Right Paddle
        if r_paddle.ycor() > 280:
            r_paddle.direction = "Down"
        if r_paddle.ycor() < -280:
            r_paddle.direction = "Up"
    elif user_choice == "multiplayer":
        pass

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce back
        ball.bounce_y()

    # Detect collision with both paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 30 and ball.ycor() > -320:
        ball.bounce_x()

    # Detect when RIGHT paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when LEFT paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == 20 or scoreboard.r_score == 20:
        game_is_on = False
        scoreboard.game_over()


my_screen.exitonclick()
