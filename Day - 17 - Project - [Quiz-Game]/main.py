from question_model import Question
from data import question_data1, question_data2
from quiz_brain import QuizBrain


def question_bank_creation(data):
    question_bank = []
    for question in data:
        question_text = question["question"]
        question_answer = question["correct_answer"]

        new_question = Question(q_text=question_text, q_answer=question_answer)
        question_bank.append(new_question)

    return question_bank


user_choice = input("\tSelect a Category for Quiz (GK/COMPUTER): ").lower()
if user_choice == "computer":
    question_bank_creation(data=question_data1)
    quiz = QuizBrain(q_list=question_bank_creation(question_data1))
    while quiz.still_has_questions():
        quiz.next_question()

    print("\tYou've completed the quiz. ")
    print(f"\tYour final score was: {quiz.score}/{quiz.question_number}")

elif user_choice == "gk":
    question_bank_creation(data=question_data2)
    quiz = QuizBrain(q_list=question_bank_creation(question_data2))
    while quiz.still_has_questions():
        quiz.next_question()

    print("\tYou've completed the quiz. ")
    print(f"\tYour final score was: {quiz.score}/{quiz.question_number}")

