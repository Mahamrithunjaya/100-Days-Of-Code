import random
from flask import Flask

random_number = random.randint(0, 9)
print(random_number)

random_colors = ['blue', 'green', 'purple', 'orange']

app = Flask(__name__)


@app.route('/')
def home():
    text = "Guess a number between 0 and 9"
    return f"<h1>{text}</h1>" \
           f"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_number:
        return f"<h1 style='color:{random.choice(random_colors)}'>{guess} is Too high, try again!</h1>" \
               f"<img src='https://media.giphy.com/media/3o7abAHdYvZdBNnGZq/source.gif'/>"
    elif guess < random_number:
        return f"<h1 style='color:red'>{guess} is Too low, try again!</h1>" \
               f"<img src='https://media.giphy.com/media/14wXMGbHjXK2k0/source.gif'/>"
    elif guess == random_number:
        return f"<h1 style='color:{random.choice(random_colors)}'>It's {guess} Correct --> You found me!!</h1>" \
               f"<img src='https://media.giphy.com/media/WAGYH6TFa8E9O/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
