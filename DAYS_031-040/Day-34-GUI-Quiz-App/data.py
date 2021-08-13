import requests
from question_model import Question
from setup_window import IntroWindow

intro = IntroWindow()
question_amount = intro.amount
question_category = intro.category
category_id = 0

if question_category == "Any Category":
    category_id = 0
elif question_category == "General Knowledge":
    category_id = 9
elif question_category == "Film":
    category_id = 11
elif question_category == "Music":
    category_id = 12
elif question_category == "Science & Nature":
    category_id = 17
elif question_category == "Computers":
    category_id = 18
elif question_category == "Mathematics":
    if question_amount == 20 or question_amount == 30:
        question_amount = 18
    category_id = 19
elif question_category == "Sports":
    if question_amount == 20 or question_amount == 30:
        question_amount = 15
    category_id = 21
elif question_category == "Animals":
    if question_amount == 20 or question_amount == 30:
        question_amount = 22
    category_id = 27
elif question_category == "Vehicles":
    if question_amount == 20 or question_amount == 30:
        question_amount = 13
    category_id = 28
elif question_category == "Mythology":
    if question_amount == 20 or question_amount == 30:
        question_amount = 10
    category_id = 20
elif question_category == "Geography":
    category_id = 22
elif question_category == "History":
    category_id = 23
elif question_category == "Politics":
    if question_amount == 20 or question_amount == 30:
        question_amount = 18
    category_id = 24

# print(intro.category)
# print(intro.amount)
# print(category_id)
parameter = {
    "amount": question_amount,
    "type": "boolean",
    "category": category_id
}


def construct_questions():
    response = requests.get(url="https://opentdb.com/api.php", params=parameter)
    response.raise_for_status()
    data = response.json()
    question_data = data["results"]

    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    return question_bank
