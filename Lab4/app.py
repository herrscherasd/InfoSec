from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:password@localhost:5432/db"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String, nullable=False)
    exp = db.Column(db.String, nullable=False)
    code = db.Column(db.String, nullable=False)
    postal = db.Column(db.String, nullable=False)
    country = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pay", methods=["POST"])
def make_payment():
    name = request.form["name"]
    number = request.form["number"]
    exp = request.form["exp"]
    code = request.form["code"]
    postal = request.form["postal"]
    country = request.form["country"]

    user = User(name=name, number=number, exp=exp, code=code, postal=postal, country=country)

    db.session.add(user)
    db.session.commit()

    return "User saved!"


if __name__ == "__main__":
    app.run(debug=True)