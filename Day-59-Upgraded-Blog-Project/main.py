import os
import smtplib

from flask import Flask, render_template, request
import requests


blog_response = requests.get(url="https://api.npoint.io/5deaf41b4f8078c817e6")
blog_response.raise_for_status()
blogs_data = blog_response.json()


MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html", all_posts=blogs_data)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form

        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", message="Successfully sent your message.")
    return render_template("contact.html", message="Contact Me")


@app.route("/post/<int:index>")
def show_post(index):
    return render_template("post.html", post_id=index, blog_posts=blogs_data)


def send_email(name, email, phone, message):

    email_message = f"Contact Me:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage: {message}"

    msg = f"From: \"{os.environ.get('SENDER_NAME')}\"<{MY_EMAIL}>\n " \
          f"To: {MY_EMAIL}\n" \
          f"Subject: New Message From {name} via my Web Form\n\n" \
          f"{email_message}".encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=120) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=msg
        )


if __name__ == "__main__":
    app.run(debug=True)
