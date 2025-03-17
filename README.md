# Holiday Countdown 🎂⏰

A web application that helps you keep track of upcoming birthdays with live countdown timers.

## 🌟 Features

- **Add Birthdays**: Easily add and manage multiple birthdays
- **Live Countdown**: Real-time countdown to each upcoming birthday
- **Responsive Design**: Mobile-friendly interface
- **Simple Management**: Edit or delete birthday entries
- **Automatic Sorting**: Birthdays automatically sorted by upcoming date

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**:
  - HTML5
  - CSS3
  - Bootstrap
  - JavaScript
- **Containerization**: Docker

## 📦 Prerequisites

- Docker
- Python 3.9+
- Git (optional)

## 🚀 Installation and Setup

### Using Docker (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/holiday-countdown.git
   cd holiday-countdown
   ```

2. Build the Docker image:
   ```bash
   docker build -t holiday-countdown .
   ```

3. Run the application:
   ```bash
   docker run -p 5000:5000 holiday-countdown
   ```

4. Open your browser and navigate to `http://localhost:5000`

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

## 🔧 Project Structure

```
holiday-countdown/
│
├── app/
│   ├── __init__.py      # Application factory
│   ├── models.py        # Database models
│   ├── routes.py        # Application routes
│   ├── templates/       # HTML templates
│   └── static/          # Static files (CSS, JS)
│
├── database/            # SQLite database storage
├── Dockerfile           # Docker configuration
├── requirements.txt     # Python dependencies
└── run.py              # Application entry point
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the Apache License. See `LICENSE` for more information.

## 📧 Contact

David Miserak - david.miserak@gmail.com

Project Link: [https://github.com/DavidMiserak/Holiday-Countdown](https://github.com/DavidMiserak/Holiday-Countdown)

## 🙏 Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
