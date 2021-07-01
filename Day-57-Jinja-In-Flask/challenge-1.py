import requests
from flask import Flask, render_template

AGE_URL = "https://api.agify.io"
GENDER_URL = "https://api.genderize.io"

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1> Go to '/guess/any_name' to use the guess feature. </h1>"


@app.route('/guess/<name>')
def guess(name):
    parameter = {
        "name": name
    }
    gender_response = requests.get(GENDER_URL, params=parameter)
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    age_response = requests.get(AGE_URL, params=parameter)
    age_response.raise_for_status()
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("challenge-1-index.html", person_name=name, gender=gender, age=age)


# ####### Another Method To DO ####### #
# def guess_gender_age(name):
#     age = requests.get(f'https://api.agify.io?name={name}').json()
#     gender = requests.get(f'https://api.genderize.io?name={name}').json()
#     data = {
#         'age': age['age'],
#         'gender': gender['gender'],
#         'name': name
#     }
#     return render_template('challenge-1-index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
