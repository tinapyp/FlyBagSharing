from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    TextAreaField,
    DateField,
    TimeField,
)
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class CreateListingForm(FlaskForm):
    departure_port = StringField("Departure Port", validators=[DataRequired()])
    arrival_port = StringField("Arrival Port", validators=[DataRequired()])
    flight_date = DateField(
        "Flight Date", format="%Y-%m-%d", validators=[DataRequired()]
    )
    flight_time = TimeField("Flight Time", format="%H:%M", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    submit = SubmitField("Post")
