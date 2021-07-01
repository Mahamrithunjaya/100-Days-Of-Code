import os

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# CREATING DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
# It will silence the deprecation warning in the console.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = os.environ.get("WEBSITE_SECRET_KEY")
db = SQLAlchemy(app)
Bootstrap(app)


# CREATING BOOK FORM
class BookForm(FlaskForm):
    book = StringField(label="Book Name", validators=[DataRequired()])
    author = StringField(label="Book Author", validators=[DataRequired()])
    rating = StringField(label="Rating", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


# CREATING RATING_EDIT FORM
class EditForm(FlaskForm):
    rating = StringField(label="New Rating", validators=[DataRequired()])
    submit = SubmitField("Change Rating")


# CREATING TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


db.create_all()


@app.route("/")
def home():
    # READ ALL RECORDS
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        # CREATING RECORD
        new_book = Book(
            title=form.book.data,
            author=form.author.data,
            rating=form.rating.data
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=form)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    form = EditForm()

    book_id = request.args.get("id")
    book_selected = Book.query.get(book_id)
    if form.validate_on_submit():
        # UPDATE RECORD
        book_selected.rating = form.rating.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit_rating.html", book=book_selected, form=form)


@app.route("/delete")
def delete():
    book_id = request.args.get("id")

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
