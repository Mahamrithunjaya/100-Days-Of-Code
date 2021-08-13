import os

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SITE_SECRET_KEY")
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps(URL)", validators=[DataRequired(), URL()])
    open_time = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close_time = StringField("Closing Time e.g. 6:30PM", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee Rating",
        choices=["✘", "☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
        validators=[DataRequired()]
    )
    wifi_rating = SelectField(
        "WIFI Rating",
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
        validators=[DataRequired()]
    )
    power_rating = SelectField(
        "Power Rating",
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', mode="a", encoding="utf8") as csv_file:
            csv_file.write(
                f"\n{form.cafe.data},"
                f"{form.location.data},"
                f"{form.open_time.data},"
                f"{form.close_time.data},"
                f"{form.coffee_rating.data},"
                f"{form.wifi_rating.data},"
                f"{form.power_rating.data}"
            )
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
