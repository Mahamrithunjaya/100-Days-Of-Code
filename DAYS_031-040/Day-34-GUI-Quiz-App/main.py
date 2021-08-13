import data
from quiz_brain import QuizBrain
from ui import QuizInterface

quiz = QuizBrain(data.construct_questions())
quiz_gui = QuizInterface(quiz)
