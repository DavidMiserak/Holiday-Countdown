# Birthday Countdown 🎂⏰

A web application that helps you keep track of upcoming birthdays with live countdown timers.

## 🌟 Features

- **Add Birthdays**: Easily add and manage multiple birthdays
- **Live Countdown**: Real-time countdown to each upcoming birthday
- **Responsive Design**: Mobile-friendly interface with Bootstrap 5
- **Simple Management**: Edit or delete birthday entries
- **Automatic Sorting**: Birthdays automatically sorted by upcoming date
- **Secure Design**: Non-root Docker container for improved security

## 🛠️ Technologies Used

- **Backend**: Flask 2.2.3 (Python)
- **Database**: SQLite with Flask-SQLAlchemy 3.0.3
- **Frontend**:
  - HTML5
  - CSS3
  - Bootstrap 5.2.3
  - JavaScript
- **Containerization**: Docker/Podman
- **Testing**: Behavior-Driven Development with Behave
- **Quality Assurance**:
  - Pre-commit hooks
  - Black code formatter
  - SQLFluff SQL linter
  - Conventional commits

## 📦 Prerequisites

- Docker/Podman
- Python 3.9+
- Git (optional)
- Firefox ESR (for running BDD tests)

## 🚀 Installation and Setup

### Using Docker/Podman (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/DavidMiserak/Birthday-Countdown.git
   cd Birthday-Countdown
   ```

2. Build and run the application using Makefile:
   ```bash
   make image-run
   ```
   This will build and run the Docker image. Open your browser and navigate to `http://localhost:5000`.

3. Alternatively, use Docker/Podman commands directly:
   ```bash
   # Build the Docker image
   docker build -t birthday-countdown .

   # Run the application
   docker run -p 5000:5000 birthday-countdown
   ```

### Local Development Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python run.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## 🧪 Running Tests

The project uses Behavior-Driven Development with Behave for testing:

```bash
# Run BDD tests with Behave
make test-bdd
```

Or run directly with:

```bash
behave tests/features
```

For more details on testing, see [TESTING.md](TESTING.md).

## 🔧 Project Structure

```
birthday-countdown/
│
├── app/
│   ├── __init__.py      # Application factory
│   ├── models.py        # Database models
│   ├── routes.py        # Application routes
│   ├── templates/       # HTML templates
│   └── static/          # Static files (CSS, JS)
│
├── database/            # SQLite database storage
├── tests/
│   └── features/        # BDD test features and steps
├── Dockerfile           # Docker configuration
├── Makefile             # Build and run commands
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── requirements.txt     # Python dependencies
└── run.py               # Application entry point
```

## 🤝 Contributing

1. Install pre-commit hooks before development:
   ```bash
   make pre-commit-setup
   ```

2. Fork the repository
3. Create your feature branch (`git checkout -b feature/AmazingFeature`)
4. Commit your changes using conventional commit messages
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## 📄 License

Distributed under the Apache License 2.0. See `LICENSE` for more information.

## 📧 Contact

David Miserak - david.miserak@gmail.com

Project Link: [https://github.com/DavidMiserak/Birthday-Countdown](https://github.com/DavidMiserak/Birthday-Countdown)

## 🙏 Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Behave](https://behave.readthedocs.io/)
- [Pre-commit](https://pre-commit.com/)
