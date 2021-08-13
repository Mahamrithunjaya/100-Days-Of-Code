class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    # TODO 3 : Checking if we're the end of the Quiz
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    # TODO 1 : Asking the Questions
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\n\tQ.{self.question_number}: {current_question.text} (True/False) : ")
        self.check_answer(user_answer, current_question.answer)

    # TODO 2 : Checking if the Answer was Correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("\tYou got it right!")
        else:
            print("\tThe answer is wrong. ")
        print(f"\tThe correct answer was : {correct_answer}. ")
        print(f"\tYour current score is : {self.score}/{self.question_number}. ")
        print("\n")
