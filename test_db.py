from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


def test_database_connection():
    try:
        with db.engine.connect():
            print("Database connection successful!")
    except Exception as e:
        print("Error connecting to the database:", str(e))


if __name__ == "__main__":
    test_database_connection()
