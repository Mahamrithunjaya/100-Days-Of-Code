import turtle
import time
import pandas


def calculate_remaining_time():
    """Calculates the seconds that is left and convert it into minutes."""
    time_taken = time.time() - startTime
    remaining_time = int(round(gameLength - time_taken))
    return time.strftime("%M:%S", time.gmtime(remaining_time))


my_screen = turtle.Screen()
my_screen.title("U.S. States Game")
my_screen.setup(width=850, height=670)
image = "blank_states_img.gif"
my_screen.addshape(image)
turtle.shape(image)
BIGTEXT = ("Arial", 20, "bold")

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.speed("fastest")

timer = turtle.Turtle()
timer.hideturtle()
timer.penup()
timer.goto(0, 250)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
score = 0
gameLength = 300  # in seconds
startTime = time.time()

while len(guessed_states) < 50:
    timer.clear()

    time_left = calculate_remaining_time()
    timer.write(arg=f"Score : {score}\n"
                    f"Time left : {time_left}", font=("Courier", 20, "bold"))

    answer_state = my_screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                       prompt="What's another state's name? Type Exit to cancel"
                                              "\nPress cancel button without any input to refresh the timer.")
    if answer_state is None:
        pass
    else:
        answer_state = answer_state.title()
    missing_states = []

    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                tim = turtle.Turtle()
                tim.hideturtle()
                tim.penup()
                missing_data = data[data.state == state]
                tim.goto(int(missing_data.x), int(missing_data.y))
                tim.color("red")
                tim.write(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        # text.goto(0, 0)
        # text.write("Review states_to_learn.csv!\n Click to close", align="center", font=BIGTEXT)
        break

    if answer_state in all_states:
        if answer_state in guessed_states:
            pass
        else:
            guessed_states.append(answer_state)
            guessed_states = list(set(guessed_states))
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
            score += 1

    if len(guessed_states) == 50:
        text.goto(-22, -229)
        text.write("Well Done! You've named them all!\n Click to close", align="center", font=BIGTEXT)

    if time.time() - startTime > gameLength:
        break

timer.clear()
timer.write(arg=f"Time Up\n"
                f"Score: {score}", font=("Courier", 20, "bold"))

text.goto(-20, -325)
text.write("See the states here or Review states_to_learn.csv!\n Click to close", align="center", font=BIGTEXT)
my_screen.exitonclick()
