from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://username:password@localhost/database_name"
)
db = SQLAlchemy(app)


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add_email", methods=["POST"])
def add_email():
    if request.method == "POST":
        email = request.form["email"]
        new_email = Email(email=email)
        db.session.add(new_email)
        db.session.commit()
        return "Email added successfully!"


if __name__ == "__main__":
    app.run(debug=True)
