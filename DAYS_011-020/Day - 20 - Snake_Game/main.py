from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from countdown import CountDown
from borders import Borders
import time

my_screen = Screen()
# Changing the background color of the Turtle Screen to Black
my_screen.setup(width=700, height=750)
my_screen.bgcolor("black")
my_screen.title(" Snake Game In PYTHON ")
# Turning the turtle animation off
my_screen.tracer(0)
sleep_time = 0

border = Borders()
border.create_borders()

user_choice = my_screen.textinput("Choose Level: ", "What level difficulty do you want? "
                                                    "(EASY / NORMAL / HARD / EXPERT)").lower()
timer_c = CountDown()

if user_choice == "easy":
    sleep_time = 0.1
elif user_choice == "normal":
    sleep_time = 0.08
elif user_choice == "hard":
    sleep_time = 0.06
elif user_choice == "expert":
    sleep_time = 0.04

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Creating the Key Strokes
my_screen.listen()
# Names of KeyArrows are Case Sensitive
my_screen.onkey(fun=snake.up, key="Up")
my_screen.onkey(fun=snake.down, key="Down")
my_screen.onkey(fun=snake.left, key="Left")
my_screen.onkey(fun=snake.right, key="Right")

play = True
while play:
    game_is_on = True
    while game_is_on:

        # Updating the turtle screen in every 0.1 second
        my_screen.update()
        time.sleep(sleep_time)  # This line says that delay for 0.1 second and then refresh the screen.

        # And every time the screen refreshes, we're going to get the snake to move forwards by one step.
        snake.move()

        p = snake.head.position()
        print(p)

        # Detect Collision with Food.
        if snake.head.distance(food) < 10:
            food.refresh_food()
            # Increasing the size of snake after each time collision with food
            snake.extend()
            # After Collision with food updating Score
            scoreboard.increase_score()

        # Detect Collision with wall.
        if snake.head.xcor() > 310 or snake.head.xcor() < -310 or snake.head.ycor() > 310 or snake.head.ycor() < -310:
            print("Collision with wall")
            scoreboard.reset_scoreboard()
            game_is_on = False
            # snake.reset_snake()

        # Detect collision with tail.
        for segment in snake.segments[1:]:
            # if head collides with any segment in the tail:
            if snake.head.distance(segment) < 5:
                # trigger game_over
                print("Collision with self")
                scoreboard.reset_scoreboard()
                game_is_on = False
                # snake.reset_snake()

    if not game_is_on:
        scoreboard.game_over()
        more = my_screen.textinput("Snake Game", "\nPlay Again: ").lower()
        if more == "yes":
            scoreboard.goto(0, 325)
            scoreboard.color("white")
            scoreboard.update_scoreboard()
            snake.reset_snake()
        else:
            play = False

my_screen.exitonclick()
