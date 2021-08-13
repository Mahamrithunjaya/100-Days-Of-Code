from tkinter import *
import data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title(f"Quizzer   -->  {data.question_category}")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Label
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 15, "bold"))
        self.score_label.grid(row=0, column=1)

        self.question_label = Label(text=f"Question: 0/0", bg=THEME_COLOR, fg="white",  font=("Arial", 15, "bold"))
        self.question_label.grid(row=0, column=0)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Questions",
                                                     fill=THEME_COLOR,
                                                     width=280,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_img,
                                   highlightthickness=0,
                                   bg=THEME_COLOR,
                                   bd=0,
                                   command=self.true_pressed)
        self.right_button.grid(row=2, column=0)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_img,
                                   highlightthickness=0,
                                   bg=THEME_COLOR,
                                   bd=0,
                                   command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        reset_img = PhotoImage(file="images/reset_image.png")
        self.reset_button = Button(image=reset_img,
                                   highlightthickness=0,
                                   bg=THEME_COLOR,
                                   bd=0,
                                   command=self.reset_quiz)
        self.reset_button.grid(row=3, column=0, columnspan=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        num, question = self.quiz.next_question()
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = question
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.buttons_state(ACTIVE)
            self.question_label.config(text=f"Question: {num}/{len(self.quiz.question_list)}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the End of the Quiz.")
            self.buttons_state(DISABLED)
            self.reset_button.config(state=ACTIVE)

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.buttons_state(DISABLED)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.buttons_state(DISABLED)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def buttons_state(self, state: str):
        self.right_button.config(state=state)
        self.wrong_button.config(state=state)

    def reset_quiz(self):
        self.quiz = QuizBrain(data.construct_questions())

        self.buttons_state(ACTIVE)
        self.reset_button.config(state=DISABLED)

        self.get_next_question()
