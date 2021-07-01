from flask import Flask, render_template
import requests

blog_response = requests.get(url="https://api.npoint.io/ed99320662742443cc5b")
blog_response.raise_for_status()
blogs_data = blog_response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("/blog_project/index.html", all_posts=blogs_data)


@app.route('/post/<int:index>')
def show_post(index):
    return render_template("/blog_project/post.html", post_id=index, blog_posts=blogs_data)


if __name__ == "__main__":
    app.run(debug=True)
