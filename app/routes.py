from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Birthday
from datetime import datetime

main = Blueprint("main", __name__)

from sqlalchemy import extract
from datetime import datetime, date


@main.route("/")
def index():
    """Display list of birthdays with countdowns, prioritizing upcoming birthdays"""
    today = date.today()

    # Custom sorting function to prioritize upcoming birthdays
    def get_next_birthday(birthday):
        # Create birthday for this year
        this_year = today.replace(month=birthday.date.month, day=birthday.date.day)

        # If this year's birthday has passed, use next year
        if this_year < today:
            this_year = this_year.replace(year=today.year + 1)

        return this_year

    # Fetch all birthdays
    birthdays = Birthday.query.all()

    # Sort birthdays by how close they are to today
    sorted_birthdays = sorted(birthdays, key=get_next_birthday)

    return render_template("index.html", birthdays=sorted_birthdays)


@main.route("/add", methods=["GET", "POST"])
def add_birthday():
    """Add a new birthday"""
    if request.method == "POST":
        name = request.form.get("name")
        date_str = request.form.get("date")

        try:
            # Convert date string to datetime object
            date = datetime.strptime(date_str, "%Y-%m-%d").date()

            # Create new birthday entry
            new_birthday = Birthday(name=name, date=date)
            db.session.add(new_birthday)
            db.session.commit()

            flash("Birthday added successfully!", "success")
            return redirect(url_for("main.index"))

        except ValueError:
            flash("Invalid date format. Please use YYYY-MM-DD.", "error")

    return render_template("add_birthday.html")


@main.route("/edit/<int:birthday_id>", methods=["GET", "POST"])
def edit_birthday(birthday_id):
    """Edit an existing birthday"""
    birthday = Birthday.query.get_or_404(birthday_id)

    if request.method == "POST":
        birthday.name = request.form.get("name")

        try:
            # Convert date string to datetime object
            date_str = request.form.get("date")
            birthday.date = datetime.strptime(date_str, "%Y-%m-%d").date()

            db.session.commit()
            flash("Birthday updated successfully!", "success")
            return redirect(url_for("main.index"))

        except ValueError:
            flash("Invalid date format. Please use YYYY-MM-DD.", "error")

    return render_template("edit_birthday.html", birthday=birthday)


@main.route("/delete/<int:birthday_id>", methods=["POST"])
def delete_birthday(birthday_id):
    """Delete a birthday"""
    birthday = Birthday.query.get_or_404(birthday_id)

    db.session.delete(birthday)
    db.session.commit()

    flash("Birthday deleted successfully!", "success")
    return redirect(url_for("main.index"))
