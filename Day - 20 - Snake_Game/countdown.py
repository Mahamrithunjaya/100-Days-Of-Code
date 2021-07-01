import time
from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 150, "bold")


class CountDown:

    def __init__(self):

        self.window = Screen()
        self.window.tracer(0)
        self.timer_text = Turtle()
        self.timer_text.color("white")
        self.timer_text.hideturtle()
        self.is_time = True
        self.start = 3
        self.update_timer()

    def update_timer(self):
        while self.is_time:
            self.timer_text.clear()
            self.timer_text.write(arg=int(self.start), align=ALIGNMENT, font=FONT)
            self.start -= 1
            self.window.update()
            time.sleep(1)
            if self.start == -1:
                self.timer_text.clear()
                self.is_time = False
