import random
import datetime
from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route('/blog/<num>')
def get_blog(num):
    blog_response = requests.get(url="https://api.npoint.io/ed99320662742443cc5b")
    blog_response.raise_for_status()
    all_posts = blog_response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
