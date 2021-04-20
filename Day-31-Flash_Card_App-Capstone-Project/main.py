from tkinter import *
from tkinter import messagebox, simpledialog
import random
import os
import pandas
from gtts import gTTS
import playsound

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
len_original_data = 0
foreign_word = ""
english_word = ""

# --------------- LANGUAGES --------------- #
LANGUAGE_CODE = {
    "Hindi": "hi",
    "Korean": "ko",
    "Nepali": "ne",
    "Bengali": "bn",
    "French": "fr"
}

available_languages = "".join([item + "\n" for item in LANGUAGE_CODE.keys()])
# --------------- POP UP WINDOW --------------- #
win2 = Tk()
win2.title("Flashy Cards Selection")
win2.config(padx=10, pady=10, bg=BACKGROUND_COLOR)
win2.minsize(width=100, height=50)
win2.withdraw()

language_2_learn = ""
ask = True
while ask:
    try:
        language_2_learn = simpledialog.askstring(title="Language to learn",
                                                  prompt="Which language would you like to learn?\t\t"
                                                         f"\nReference Language is set to English").title()
    except AttributeError:
        exit()
    if language_2_learn in LANGUAGE_CODE.keys():
        ask = False
    else:
        messagebox.showerror(title="Wrong Language", message="Please, add a valid language between:\n"
                                                             f"{available_languages}")

win2.destroy()
# --------------- CSV DATA READ --------------- #
try:
    data = pandas.read_csv(f"data/words_to_learn_{language_2_learn}.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    # global len_original_data
    original_data = pandas.read_csv(f"data/{language_2_learn}_words.csv")
    len_original_data = len(original_data)
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")


# --------------- NEXT CARD --------------- #
def next_card():
    """Display the card front with the foreign word"""
    global current_card, flip_timer, foreign_word, english_word
    right_button.config(state="disabled")
    wrong_button.config(state="disabled")
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    foreign_word = current_card[language_2_learn]
    english_word = current_card["English"]
    canvas.itemconfig(card_background, image=front_image)
    canvas.itemconfig(card_title, text=language_2_learn, fill="black")
    canvas.itemconfig(card_word, text=foreign_word, fill="black")

    # Play Audio of word using Google Text-to-Speech
    audio_output = gTTS(text=foreign_word, lang=LANGUAGE_CODE[language_2_learn])
    audio_output.save("foreign_word.mp3")
    playsound.playsound("foreign_word.mp3", True)
    os.remove("foreign_word.mp3")

    flip_timer = window.after(4000, func=flip_card)


# --------------- FLIP CARD --------------- #
def flip_card():
    """Display the card back with the English word"""
    wrong_button.config(state="active")
    right_button.config(state="active")

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(card_background, image=back_image)

    # Play Audio of word using Google Text-to-Speech
    audio_output = gTTS(text=english_word, lang="en")
    audio_output.save("english_word.mp3")
    playsound.playsound("english_word.mp3", True)
    os.remove("english_word.mp3")


# ---------- If the user know the English Translation of the Word ---------- #
def is_known():
    """Remove learnt words from the list of remaining words.
    Save the remaining words and display the next card.
    If there are no more words, then display messagebox and exit"""
    if len(to_learn) >= 1:
        to_learn.remove(current_card)
        print(len(to_learn))
        data2 = pandas.DataFrame(to_learn)
        data2.to_csv(f"data/words_to_learn_{language_2_learn}.csv", index=False)
    if len(to_learn) != 0:
        next_card()
    else:
        messagebox.showinfo(title="Complete", message="Well done !\nYou have completed the Flash Cards.")
        window.after(2000, func=exit())


def start_game():
    start_button.config(state=DISABLED)
    canvas.delete(card_convert)
    canvas.itemconfig(card_title, font=("Ariel", 40, "italic"), text="")
    canvas.itemconfig(card_word, font=("Ariel", 60, "bold"), text="")
    next_card()


# --------------------------------------------------- UI SETUP ------------------------------------------------------ #
window = Tk()
window.title(f"Flash Card App     {language_2_learn} - English")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# ---------- TIMER TO FLIP CARD ---------- #
flip_timer = window.after(3000, func=flip_card)
window.after_cancel(flip_timer)
# Canvas
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="image/card_front.png")
back_image = PhotoImage(file="image/card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, font=("Ariel", 60, "italic"), text=language_2_learn)
card_convert = canvas.create_text(400, 217, font=("Ariel", 30, "italic"), text="TO")
card_word = canvas.create_text(400, 283, font=("Ariel", 40, "bold"), text="ENGLISH")
# To show the score
# card_number = canvas.create_text(680, 50, text=f"{}/{len_original_data}", font=("Ariel", 25, "normal"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=3)

# Buttons
wrong_image = PhotoImage(file="image/wrong.png")
wrong_button = Button(
    image=wrong_image,
    bg=BACKGROUND_COLOR,
    borderwidth=0,
    highlightthickness=0,
    relief=FLAT,
    state=DISABLED,
    command=next_card
)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="image/right.png")
right_button = Button(
    image=right_image,
    bg=BACKGROUND_COLOR,
    borderwidth=0,
    highlightthickness=0,
    relief=FLAT,
    state=DISABLED,
    command=is_known
)
right_button.grid(column=2, row=1)

start_image = PhotoImage(file="image/start_img.png")
start_button = Button(
    image=start_image,
    bg=BACKGROUND_COLOR,
    borderwidth=0,
    highlightthickness=0,
    relief=FLAT,
    state=ACTIVE,
    command=start_game
)
start_button.grid(column=1, row=1)

window.mainloop()
