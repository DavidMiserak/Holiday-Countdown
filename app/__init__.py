from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)

    # Ensure database directory exists
    base_dir = os.path.abspath(os.path.dirname(__file__))
    database_dir = os.path.join(base_dir, "..", "database")
    os.makedirs(database_dir, exist_ok=True)

    # Configuration
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "your_secret_key_here")
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f'sqlite:///{os.path.join(database_dir, "birthdays.db")}'
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize database
    from .models import db

    db.init_app(app)

    # Create database tables
    with app.app_context():
        db.create_all()

    # Register blueprints
    from .routes import main

    app.register_blueprint(main)

    return app
