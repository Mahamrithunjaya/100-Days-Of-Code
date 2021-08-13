import random
from distutils.util import strtobool

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Dictionary Comprehension
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    all_cafe = db.session.query(Cafe).all()
    random_cafe = random.choice(all_cafe)

    # return jsonify(cafe={
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "seats": random_cafe.seats,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "has_sockets": random_cafe.has_sockets,
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price,
    # })

    # return jsonify(cafe={
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #
    #     "amenities": {
    #         "seats": random_cafe.seats,
    #         "has_toilet": random_cafe.has_toilet,
    #         "has_wifi": random_cafe.has_wifi,
    #         "has_sockets": random_cafe.has_sockets,
    #         "can_take_calls": random_cafe.can_take_calls,
    #         "coffee_price": random_cafe.coffee_price,
    #     }
    # })

    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def get_cafe_at_location():
    if "loc" in request.args:
        search_location = request.args.get("loc").title()
        # search_wifi = request.args.get("wifi")
        print(search_location)
        cafes = Cafe.query.filter_by(location=search_location).all()
        if cafes:
            return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
        else:
            return jsonify(Error={"Not found": "Sorry, we don't have a cafe at that location."}), 400
    else:
        return jsonify(Error={"No Field": "No location field provided. Please specify the location."}), 418


@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(strtobool(request.form.get('toilet'))),
        has_wifi=bool(strtobool(request.form.get("wifi"))),
        has_sockets=bool(strtobool(request.form.get("sockets"))),
        can_take_calls=bool(strtobool(request.form.get("calls"))),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"Success": "Successfully added the new cafe. "})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    if "new_price" in request.args:
        update_price = request.args.get("new_price")
        cafe = db.session.query(Cafe).get(cafe_id)

        if cafe:
            cafe.coffee_price = update_price
            db.session.commit()
            # 200 = OK
            return jsonify(Response={"Success": "Successfully updated the price."}), 200
        else:
            # 400 = Resource Not Found
            return jsonify(Error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 400
    else:
        return jsonify(Error={"No Field": "No update-price field provided. Please provide a update-price field."}), 400


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_closed_cafe(cafe_id):
    if "api-key" in request.args:
        api_key = request.args.get("api-key")
        if api_key == "TopSecretAPIKey":
            cafe = db.session.query(Cafe).get(cafe_id)

            if cafe:
                db.session.delete(cafe)
                db.session.commit()
                return jsonify(Response={"Success": "Successfully Deleted the cafe from the database."}), 200
            else:
                return jsonify(Error={"Not Found": "Sorry a cafe with that id is not found in the database."}), 400
        else:
            return jsonify(Error={
                "Forbidden": "Sorry, that's not allowed. Make sure that you have the correct api_key."
            }), 403
    else:
        return jsonify(Error={"No Field": "No api-key field provided. Please provide a api-key field. "}), 418


if __name__ == '__main__':
    app.run(debug=True)
