from flask import Flask, render_template, request
from datetime import datetime, date
import pytz

app = Flask(__name__)


def calculate_next_birthday(birthday):
    """
    Calculate the date of the next birthday.

    :param birthday: datetime object representing the birthday
    :return: datetime object of the next birthday
    """
    today = date.today()
    next_birthday = birthday.replace(year=today.year)

    # If this year's birthday has passed, use next year
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    return next_birthday


def get_countdown(birthday):
    """
    Calculate the time remaining until the next birthday.

    :param birthday: datetime object representing the birthday
    :return: dictionary with days, hours, minutes, seconds remaining
    """
    today = datetime.now(pytz.UTC)

    # Convert birthday to datetime with current year
    next_birthday = datetime.combine(
        calculate_next_birthday(birthday.date()), datetime.min.time()
    ).replace(tzinfo=pytz.UTC)

    # Calculate time difference
    time_to_birthday = next_birthday - today

    # Extract components
    days = time_to_birthday.days
    hours, remainder = divmod(time_to_birthday.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return {"days": days, "hours": hours, "minutes": minutes, "seconds": seconds}


@app.route("/", methods=["GET", "POST"])
def birthday_countdown():
    countdown = None
    birthday = None
    error = None

    if request.method == "POST":
        try:
            # Parse birthday from form
            birthday_str = request.form["birthday"]
            birthday = datetime.strptime(birthday_str, "%Y-%m-%d")

            # Localize to UTC to avoid timezone issues
            birthday = birthday.replace(tzinfo=pytz.UTC)

            # Calculate countdown
            countdown = get_countdown(birthday)
        except ValueError:
            error = "Invalid date format. Please use YYYY-MM-DD."

    return render_template(
        "index.html", countdown=countdown, birthday=birthday, error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
