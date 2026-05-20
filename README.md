# 💼 Investment Management System

> A secure Flask web application for tracking personal investments — with user authentication, profit/loss calculation, and a clean dashboard interface.

---

## 📌 Overview

Investment Management System is a full-stack web application built with **Python (Flask)** and **SQLite**. It allows users to securely log in and manage their investment portfolio — tracking assets by name, type, quantity, buy price, and current price, with automatic profit/loss calculation.

---

## ✨ Features

- 🔐 **Secure User Authentication** — Login/logout with hashed passwords using Flask-Bcrypt
- 📊 **Investment Dashboard** — View all tracked investments in one place
- ➕ **Add Investments** — Record assets with name, type, quantity, buy price, and current price
- ✏️ **Edit Investments** — Update existing investment details
- 📈 **Profit/Loss Calculation** — Automatically computed per investment: `(current_price − buy_price) × quantity`
- 🗄️ **SQLite Database** — Lightweight persistent storage with SQLAlchemy ORM
- 🌐 **AJAX Login** — Smooth login flow using `fetch()` without page reload

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| Auth | Flask-Login, Flask-Bcrypt |
| ORM / Database | Flask-SQLAlchemy, SQLite |
| Frontend | HTML5, CSS3, Jinja2 Templates |
| API Style | REST (AJAX via `fetch()`) |

---

## 📁 Project Structure

```
Investment-management-system/
│
├── app.py                   # Main Flask app — routes, auth, DB init
│
├── templates/               # HTML templates (Jinja2)
│   ├── index.html           # Landing / home page
│   ├── login.html           # Login form with AJAX submit
│   ├── dashboard.html       # Investment dashboard (login-protected)
│   └── edit.html            # Edit investment form
│
├── static/                  # Static assets
│   └── style.css            # Application stylesheet
│
├── instance/                # Auto-created at runtime (gitignored)
│   └── users.db             # SQLite database file
│
├── __pycache__/             # Python bytecode cache (gitignored)
│   ├── app.cpython-311.pyc
│   └── models.cpython-311.pyc
│
├── requirements.txt         # Python dependencies
├── .gitignore               # Excludes instance/, __pycache__, .env
└── README.md                # Project documentation
```

---

## ⚙️ How It Works

```
User visits /login
       ↓
Enters credentials → fetch() POST to /api/login
       ↓
Flask-Bcrypt verifies hashed password in SQLite
       ↓
Flask-Login creates session → redirect to /dashboard
       ↓
Dashboard renders all Investment records for the user
       ↓
User can Add / Edit investments
       ↓
profit_loss() = (current_price − buy_price) × quantity
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/keerthi-yk/Investment-management-system.git
cd Investment-management-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

> The app auto-creates the SQLite database and seeds a default admin user on first run.

---

## 🔑 Default Login Credentials

| Field | Value |
|---|---|
| Username | `admin` |
| Password | `admin123` |

> ⚠️ Change the `SECRET_KEY` and default credentials before deploying to production.

---

## 📦 Dependencies

```
flask
flask_sqlalchemy
flask_login
flask-bcrypt
```

Install all with:

```bash
pip install flask flask_sqlalchemy flask_login flask-bcrypt
```

---

## 🔮 Future Improvements

- [ ] Per-user investment isolation (user_id filtering on dashboard)
- [ ] Live stock price integration via a financial API
- [ ] Portfolio summary — total invested, total current value, net P&L
- [ ] Charts and graphs for portfolio performance over time
- [ ] Export investments as CSV / PDF report
- [ ] Password change and user profile management

---

[![GitHub](https://img.shields.io/badge/GitHub-keerthi--yk-181717?style=flat&logo=github)](https://github.com/keerthi-yk)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-keerthi--yk-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/keerthi-yk)
[![Email](https://img.shields.io/badge/Email-keerthi.yk79@gmail.com-D14836?style=flat&logo=gmail)](mailto:keerthi.yk79@gmail.com)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
