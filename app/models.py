from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    listings = db.relationship("Listing", backref="author", lazy=True)


class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departure_port = db.Column(db.String(100), nullable=False)
    arrival_port = db.Column(db.String(100), nullable=False)
    flight_date = db.Column(db.Date, nullable=False)
    flight_time = db.Column(db.Time, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
