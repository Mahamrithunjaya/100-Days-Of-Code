from tkinter import *
from tkinter import messagebox
import winsound
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#79d70f"
YELLOW = "#edf285"
FONT_NAME = "Courier"
WORK_MIN = 8
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 5
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    start_button.config(state=ACTIVE)
    reset_button.config(state=DISABLED)
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_label.config(text="")


# ------------------------- POP-UP WINDOW MECHANISM ------------------------- #
def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button.config(state=DISABLED)
    reset_button.config(state=ACTIVE)
    global reps
    print(reps)
    reps += 1

    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    # If it's the 1st/3rd/5th/7th reps then WORK
    # If it's the 8th reps then LONG_BREAK
    # If it's 2nd/4th/6th reps then SHORT_BREAK
    if reps % 8 == 0:
        focus_window("on")
        messagebox.showinfo(title="Break", message="Long Break~")
        countdown(long_break_sec)
        winsound.Beep(1000, 1000)
        title_label.config(text="Long-Break", fg=RED)
    elif reps % 2 == 0:
        focus_window("on")
        messagebox.showinfo(title="Break", message="Small Break~")
        countdown(short_break_sec)
        winsound.Beep(1000, 1000)
        title_label.config(text="Short-Break", fg=PINK)
    else:
        focus_window("off")
        messagebox.showinfo(title="Work", message="Start working~")
        countdown(work_sec)
        winsound.Beep(1000, 1000)
        title_label.config(text="Work", fg=GREEN)

    if reps == 9:
        reset_timer()
        focus_window("off")
        messagebox.showinfo(title="DONE", message="1st Full Round Complete~\n\nTo begin with 2nd Round Start again.")


# ----------------------- MESSAGE BOX POP-UP MECHANISM -------------------------- #
def raise_window(msg_box):
    msg_box.attributes('-topmost', 1)
    msg_box.attributes('-topmost', 0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        raise_window(msg_box=window)
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)

title_label = Label(text="Timer", width=12, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "italic"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer, state=ACTIVE)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer, state=DISABLED)
reset_button.grid(column=2, row=2)

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
check_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
