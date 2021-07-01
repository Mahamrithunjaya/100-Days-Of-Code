import os
from datetime import datetime as dt

from flask import Flask, render_template, redirect, url_for, flash, abort, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from flask_gravatar import Gravatar
from functools import wraps
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SITE_SECRET_KEY")
ckeditor = CKEditor(app)
Bootstrap(app)

gravatar = Gravatar(
    app,
    size=100,
    rating="g",
    default="retro",
    force_default=False,
    force_lower=False,
    use_ssl=False,
    base_url=None
)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get("GMAIL_USERID")
app.config['MAIL_PASSWORD'] = os.environ.get("GMAIL_USER_PASS")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CREATING ADMIN-ONLY DECORATOR
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)
    return decorated_function


# CREATING THE USERS TABLE
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

    posts = relationship("BlogPost", back_populates="author")

    # "comment_author" refers to the comment_author property in the Comment class.
    comments = relationship("Comment", back_populates="comment_author")


# CREATE ALL THE TABLES IN THE DATABASE
db.create_all()


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)

    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")

    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    comments = relationship("Comment", back_populates="parent_post")


db.create_all()


# CREATING COMMENTS TABLE
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    comment_date = db.Column(db.String(250), nullable=False)
    comment_time = db.Column(db.String(250), nullable=False)

    # "users.id" The users refers to the tablename of the Users class.
    # "comments" refers to the comments property in the User class.
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")

    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")
    text = db.Column(db.Text, nullable=False)


db.create_all()


# DISPLAYING THE CURRENT YEAR ON THE WEBPAGE
CURRENT_YEAR = dt.now().year


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts, current_user=current_user, year=CURRENT_YEAR)


# REGISTER NEW USERS INTO THE USER DATABASE
@app.route('/register', methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():

        # IF USER'S EMAIL ALREADY EXISTS
        if User.query.filter_by(email=register_form.email.data).first():
            # Send Flash Message
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))

        hash_and_salted_password = generate_password_hash(
            register_form.password.data,
            method="pbkdf2:sha256",
            salt_length=8
        )

        new_user = User(
            email=register_form.email.data,
            name=register_form.name.data,
            password=hash_and_salted_password
        )
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for("get_all_posts"))

    return render_template("register.html", form=register_form, current_user=current_user, year=CURRENT_YEAR)


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        # Find the user by email entered
        user = User.query.filter_by(email=email).first()

        # Email doesn't Exist
        if not user:
            flash("That Email does not exist, Please try again.")
            return redirect(url_for("login"))
        # Password Incorrect
        elif not check_password_hash(user.password, password):
            flash("Password Incorrect, Please try again.")
            return redirect(url_for("login"))
        # Email exists and Password Correct
        else:
            login_user(user)
            return redirect(url_for("get_all_posts"))

    return render_template("login.html", form=login_form, current_user=current_user, year=CURRENT_YEAR)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    comment_form = CommentForm()
    requested_post = BlogPost.query.get(post_id)

    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("First you need to login or register to make any comments.")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=comment_form.comment.data,
            comment_author=current_user,
            comment_date=dt.now().strftime("%B %d,%Y"),
            comment_time=dt.now().strftime("%I:%M %p"),
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()

    # Clear comment form after it is submitted - Two Ways to do it:
    # Method 1-
        return redirect(url_for("show_post", post_id=post_id))

    # Method 2-
    # comment_form.comment.data = ""

    return render_template("post.html", post=requested_post, current_user=current_user, form=comment_form,
                           year=CURRENT_YEAR)


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user, year=CURRENT_YEAR)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", current_user=current_user, year=CURRENT_YEAR)
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")

        msg = Message(
            subject=f"Subhajit's Blog - New Mail from {name}",
            body=f"Name: {name}\nE-Mail: {email}\nPhone: {phone}\n\nIP-Address: {request.remote_addr}\n"
                 f"IP-User: {request.remote_user}\nDate: {dt.now()}\n\nMessage: {message}",
            sender=email,
            recipients=[os.environ.get("GMAIL_USERID")]
        )
        mail.send(msg)
        return render_template("contact.html", current_user=current_user, year=CURRENT_YEAR, success=True)


@app.route("/new-post", methods=["POST", "GET"])
@admin_only
def add_new_post():
    post_form = CreatePostForm()
    if post_form.validate_on_submit():
        new_post = BlogPost(
            title=post_form.title.data,
            subtitle=post_form.subtitle.data,
            body=post_form.body.data,
            img_url=post_form.img_url.data,
            author_id=current_user.id,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=post_form, current_user=current_user, year=CURRENT_YEAR)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user, year=CURRENT_YEAR)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/delete-comment/<int:post_id>/<int:comment_id>")
@login_required
def delete_comment(post_id, comment_id):
    comment_to_delete = Comment.query.get(comment_id)
    db.session.delete(comment_to_delete)
    db.session.commit()
    return redirect(url_for("show_post", post_id=post_id))


# ######################### Another Way to Delete Comments #############################
# @app.route("/delete-comment/<int:comment_id>")
# @login_required
# def delete_comment(comment_id):
#     comment_to_delete = Comment.query.filter_by(id=comment_id).first()
#     post_to_return = BlogPost.query.filter_by(id=comment_to_delete.post_id).first()
#     db.session.delete(comment_to_delete)
#     db.session.commit()
#     return redirect(url_for("show_post", post_id=post_to_return.id))
#
# ########## Replace the current <a> of post.html with this in comment area. ##########
# <a href="{{url_for('delete_comment', comment_id=comment.id) }}">✘</a>
#
# ######################################################################################


@app.route("/number-of-users-view")
@login_required
@admin_only
def show_users_list():
    all_users = User.query.all()
    return render_template("users-list.html", users=all_users)


@app.route("/delete-user/<int:user_id>")
@login_required
def delete_user(user_id):
    user_to_delete = User.query.get(user_id)
    comments_to_delete = Comment.query.filter_by(author_id=user_id).delete()
    db.session.delete(user_to_delete)
    db.session.commit()
    return redirect(url_for("show_users_list", user_id=user_id))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
