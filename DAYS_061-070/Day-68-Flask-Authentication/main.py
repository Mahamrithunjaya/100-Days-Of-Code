import os

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("WEBAPP_SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    # Every render_template has a logged_in variable set.
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":

        if User.query.filter_by(email=request.form.get("email")).first():
            # User already Exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))

        hash_and_salted_password = generate_password_hash(
            request.form.get("password"),
            method="pbkdf2:sha256",
            salt_length=8
        )

        new_user = User(
            email=request.form.get("email"),
            name=request.form.get("name"),
            password=hash_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user after adding details to database.
        login_user(new_user)

        return redirect(url_for("secrets", name=new_user.name))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Find the user by email entered
        user = User.query.filter_by(email=email).first()

        # Email doesn't Exist
        if not user:
            flash("That email doesn't exist, please try again")
            return redirect(url_for("login"))
        # Password Incorrect
        elif not check_password_hash(user.password, password):
            flash("Password Incorrect, please try again.")
            return redirect(url_for("login"))
        # Email exists and Password Correct
        else:
            login_user(user)
            return redirect(url_for("secrets", name=user.name))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download/<path:filename>')
@login_required
def download(filename):
    return send_from_directory(
        directory="static/files",
        path=filename,
        as_attachment=False
    )
    # OR
    # return send_from_directory("static", path="files/cheat_sheet.pdf", as_attachment=False)


if __name__ == "__main__":
    app.run(debug=True)
