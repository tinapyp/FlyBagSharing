from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, URL
import os

app = Flask(__name__)
db_url = URL.create(
    drivername="postgresql",
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    database=os.getenv("POSTGRES_DATABASE"),
)
app.config["SQLALCHEMY_DATABASE_URI"] = db_url
db = SQLAlchemy(app)


class Email(db.Model):
    __tablename__ = "waiting_list"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add_email", methods=["POST"])
def add_email():
    if request.method == "POST":
        email = request.form["email"]
        try:
            new_email = Email(email=email)
            db.session.add(new_email)
            db.session.commit()
            return "Email added successfully!"
        except Exception as e:
            db.session.rollback()
            return f"Failed to add email: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
