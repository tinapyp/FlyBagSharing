from flask import render_template, url_for, flash, redirect, request, abort
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, CreateListingForm
from app.models import User, Listing
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    listings = Listing.query.all()
    return render_template("index.html", listings=listings)


@app.route("/new_listing", methods=["GET", "POST"])
@login_required
def new_listing():
    form = CreateListingForm()
    if form.validate_on_submit():
        listing = Listing(
            departure_port=form.departure_port.data,
            arrival_port=form.arrival_port.data,
            flight_date=form.flight_date.data,
            flight_time=form.flight_time.data,
            description=form.description.data,
            phone_number=form.phone_number.data,
            author=current_user,
        )
        db.session.add(listing)
        db.session.commit()
        flash("Your listing has been created!", "success")
        return redirect(url_for("home"))
    return render_template("create_listing.html", title="New Listing", form=form)


@app.route("/listing/<int:listing_id>/delete", methods=["POST"])
@login_required
def delete_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    if listing.author != current_user:
        abort(403)
    db.session.delete(listing)
    db.session.commit()
    flash("Your listing has been deleted!", "success")
    return redirect(url_for("home"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
        )
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in", "success")
        return redirect(url_for("login"))
    return render_template("signup.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))
