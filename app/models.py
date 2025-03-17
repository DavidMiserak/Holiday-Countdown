from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Birthday(db.Model):
    """Model for storing birthday information"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Birthday {self.name} on {self.date}>"

    def next_birthday(self):
        """Calculate the next occurrence of this birthday"""
        today = datetime.now().date()
        this_year_birthday = self.date.replace(year=today.year)

        if this_year_birthday < today:
            # If this year's birthday has passed, use next year
            return this_year_birthday.replace(year=today.year + 1)
        return this_year_birthday
