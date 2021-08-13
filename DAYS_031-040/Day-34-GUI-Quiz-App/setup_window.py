from tkinter import ttk, messagebox
from tkinter import *

THEME_COLOR = "#375362"


class IntroWindow:

    def __init__(self):
        self.category = ""
        self.amount = 0

        self.window = Tk()
        self.window.config(width=400, height=200, padx=50, pady=50, bg=THEME_COLOR)
        self.window.title("Quizzer Setup")

        self.question_label = Label(text="Select Number of Questions:", bg=THEME_COLOR, fg="white",
                                    font=("Roboto", 15, "bold"))
        self.question_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.radio_state = IntVar()
        self.radio_button_1 = Radiobutton(text="10",
                                          font=("Roboto", 12, "bold"),
                                          value=10,
                                          variable=self.radio_state,
                                          bg=THEME_COLOR,
                                          command=self.radio_used)
        self.radio_button_2 = Radiobutton(text="20",
                                          font=("Roboto", 12, "bold"),
                                          value=20,
                                          variable=self.radio_state,
                                          bg=THEME_COLOR,
                                          command=self.radio_used)
        self.radio_button_3 = Radiobutton(text="30",
                                          font=("Roboto", 12, "bold"),
                                          value=30,
                                          variable=self.radio_state,
                                          bg=THEME_COLOR,
                                          command=self.radio_used)
        self.radio_button_1.grid(row=1, column=0)
        self.radio_button_2.grid(row=1, column=1)
        self.radio_button_3.grid(row=1, column=2)

        self.category_label = Label(text="Select Category: ", bg=THEME_COLOR, fg="white", font=("Roboto", 15, "bold"))
        self.category_label.grid(row=2, column=0, pady=20, columnspan=2)

        self.box_value = StringVar()
        self.combo_box = ttk.Combobox(self.window, textvariable=self.box_value, height=14, foreground="black",
                                      font=("Arial", 12))
        self.combo_box['values'] = (
            'Any Category',
            'General Knowledge',
            'Film',
            'Music',
            'Science & Nature',
            'Computers',
            'Mathematics',
            'Sports',
            'Animals',
            'Vehicles',
            'Mythology',
            'Geography',
            'History',
            'Politics'
        )
        self.combo_box['state'] = 'readonly'
        self.combo_box.grid(row=3, column=0, columnspan=3, sticky=EW)
        self.combo_box.current(0)
        self.combo_box.bind('<<ComboboxSelected>>', self.combobox_used)

        self.submit_button = Button(text="SUBMIT", font=("Roboto", 15, "bold"), command=self.submit_button_pressed)
        self.submit_button.grid(row=4, column=0, pady=20, columnspan=3)

        self.window.mainloop()

    def radio_used(self):
        self.amount = self.radio_state.get()

    def combobox_used(self, event):
        self.category = self.combo_box.get()

    def submit_button_pressed(self):
        if self.amount == 0:
            messagebox.showerror(title="Choice Error !!", message="You selected nothing from\nthe Amount section.")

        if self.category == "Mathematics":
            if self.amount == 20 or self.amount == 30:
                messagebox.showinfo(title="Available of Questions",
                                    message="Your selected amount(number) of\nquestions not available."
                                            "\n\nMax 18 questions are available for this Category."
                                            "\n\nSo Questions are set to MAX of Available Questions."
                                    )
        elif self.category == "Sports":
            if self.amount == 20 or self.amount == 30:
                messagebox.showinfo(title="Available of Questions",
                                    message="Your selected amount(number) of\nquestions not available."
                                            "\n\nMax 15 questions are available for this Category."
                                            "\n\nSo Questions are set to MAX of Available Questions."
                                    )
        elif self.category == "Vehicles":
            if self.amount == 20 or self.amount == 30:
                messagebox.showinfo(title="Available of Questions",
                                    message="Your selected amount(number) of\nquestions not available."
                                            "\n\nMax 13 questions are available for this Category."
                                            "\n\nSo Questions are set to MAX of Available Questions."
                                    )
        elif self.category == "Politics":
            if self.amount == 20 or self.amount == 30:
                messagebox.showinfo(title="Available of Questions",
                                    message="Your selected amount(number) of\nquestions not available."
                                            "\n\nMax 18 questions are available for this Category."
                                            "\n\nSo Questions are set to MAX of Available Questions."
                                    )
        elif self.category == "Mythology":
            if self.amount == 20 or self.amount == 30:
                messagebox.showinfo(title="Available of Questions",
                                    message="Your selected amount(number) of\nquestions not available."
                                            "\n\nOnly 10 questions are available for this Category."
                                            "\n\nSo Questions are set to MAX of Available Questions."
                                    )
        elif self.category == "Animals":
            if self.amount == 20 or self.amount == 30:
                messagebox.showinfo(title="Available of Questions",
                                    message="Your selected amount(number) of\nquestions not available."
                                            "\n\nMax 22 questions are available for this Category."
                                            "\n\nSo Questions are set to MAX of Available Questions."
                                    )

        self.window.destroy()
