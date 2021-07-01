from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        text = function()
        return f"<strong>{text}</strong>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        text = function()
        return f"<em>{text}<em>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        text = function()
        return f"<u>{text}<u>"

    return wrapper_function


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(debug=True)
