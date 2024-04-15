from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("POSTGRES_URL")
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
        try:
            db.engine.execute(f"INSERT INTO waiting_list (email) VALUES ('{email}')")
            return "Email added successfully!"
        except Exception as e:
            return f"Failed to add email: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
