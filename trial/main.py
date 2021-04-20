from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
from math import atan2, degrees

# Create screen object
s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong")
s.tracer(0)

# Create paddles, ball and scoreboard
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
score = Scoreboard()

# Game speed parameters
default_game_speed = 0.02
game_acceleration = 1.05

# Initialize settings
game_speed = default_game_speed
paddle_hit = False
game_is_on = True
s.update()
time.sleep(1)

# Keyboard input
s.listen()
s.getcanvas().bind("<Up>", r_paddle.move_up_true)
s.getcanvas().bind("<KeyRelease-Up>", r_paddle.move_up_false)
s.getcanvas().bind("<Down>", r_paddle.move_down_true)
s.getcanvas().bind("<KeyRelease-Down>", r_paddle.move_down_false)
s.getcanvas().bind("<z>", l_paddle.move_up_true)
s.getcanvas().bind("<KeyRelease-z>", l_paddle.move_up_false)
s.getcanvas().bind("<s>", l_paddle.move_down_true)
s.getcanvas().bind("<KeyRelease-s>", l_paddle.move_down_false)

while game_is_on:
    time.sleep(game_speed)
    r_paddle.move_up(r_paddle.ycor())
    l_paddle.move_up(l_paddle.ycor())
    r_paddle.move_down(r_paddle.ycor())
    l_paddle.move_down(l_paddle.ycor())
    ball.forward(5)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_border()
    if not paddle_hit:
        if (350 > ball.xcor() > 330) and ball.distance(r_paddle) < 50:
            new_heading = degrees(atan2(ball.ycor() - r_paddle.ycor(), ball.xcor() - r_paddle.xcor()))
            if new_heading < 0:
                new_heading = new_heading + 360
            new_heading = ((new_heading - 180) * 0.6) + 180
            ball.setheading(new_heading)
            game_speed *= 1 / game_acceleration
            paddle_hit = True
        if (-350 < ball.xcor() < -330) and ball.distance(l_paddle) < 50:
            new_heading = degrees(atan2(ball.ycor() - l_paddle.ycor(), ball.xcor() - l_paddle.xcor()))
            new_heading *= 0.6
            ball.setheading(new_heading)
            game_speed *= 1 / game_acceleration
            paddle_hit = True
    else:
        if -320 < ball.xcor() < 320:
            paddle_hit = False
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        score.update()
        s.update()
        game_speed = default_game_speed
        time.sleep(1)
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        score.update()
        s.update()
        game_speed = default_game_speed
        time.sleep(1)
    s.update()

s.exitonclick()
