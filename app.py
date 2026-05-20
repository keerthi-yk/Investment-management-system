"""Minimal but complete Flask backend for the Investment Manager login flow.
Run with `python app.py` (dev) or `flask run`.
Requires: flask, flask_sqlalchemy, flask_login, flask-bcrypt
Install once: pip install flask flask_sqlalchemy flask_login flask-bcrypt
"""
from __future__ import annotations

import os
from pathlib import Path

from flask import (
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_bcrypt import Bcrypt
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy



# -----------------------------------------------------------------------------
# App + extensions ----------------------------------------------------------------
# -----------------------------------------------------------------------------
BASE_DIR = Path(__file__).parent.resolve()
DB_DIR = BASE_DIR / "instance"
DB_PATH = DB_DIR / "users.db"
DB_URI = f"sqlite:///{DB_PATH.as_posix()}"

# Ensure ./instance exists so SQLite can create the file without permission errors
DB_DIR.mkdir(exist_ok=True)

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.update(
    SECRET_KEY="replace-this-in-production",  # Used for session cookies
    SQLALCHEMY_DATABASE_URI=DB_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# Initialise extensions
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "show_login"  # Redirect here for @login_required

# SQLAlchemy must be initialised *after* app config
db = SQLAlchemy(app)

# -----------------------------------------------------------------------------
# Models -----------------------------------------------------------------------
# -----------------------------------------------------------------------------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    pwd_hash = db.Column(db.String(128), nullable=False)

    # Helper factory
    @classmethod
    def create(cls, username: str, password: str) -> "User":
        return cls(
            username=username,
            pwd_hash=bcrypt.generate_password_hash(password).decode(),
        )

    # Password check
    def verify_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.pwd_hash, password)


@login_manager.user_loader
def load_user(user_id: str):
    return User.query.get(int(user_id)) if user_id.isdigit() else None


# -----------------------------------------------------------------------------
# One‑time database creation & seed user ---------------------------------------
# -----------------------------------------------------------------------------
with app.app_context():
    db.create_all()  # Creates the tables if missing

    if not User.query.filter_by(username="admin").first():
        db.session.add(User.create("admin", "admin123"))
        db.session.commit()
        app.logger.info("Seeded default user: admin / admin123")


# -----------------------------------------------------------------------------
# Routes -----------------------------------------------------------------------
# -----------------------------------------------------------------------------
@app.route("/login")
def show_login():
    """Serve the login page (GET)"""
    if current_user.is_authenticated:
        # Already logged in → dashboard
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.post("/api/login")
def api_login():
    """AJAX endpoint called by login.html via fetch()."""
    payload = request.get_json(force=True)
    username = (payload or {}).get("username", "").strip()
    password = (payload or {}).get("password", "")

    user = User.query.filter_by(username=username).first()
    if user and user.verify_password(password):
        login_user(user)
        return jsonify(ok=True)

    return jsonify(message="Invalid credentials"), 401


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("show_login"))


@app.route("/dashboard")
@login_required
def dashboard():
    # Render a simple placeholder dashboard; replace with your existing page.
    return (
        f"<h1 style='font-family:system-ui'>Welcome {current_user.username} 🎉</h1>"
        "<p><a href='/logout'>Logout</a></p>"

    )

from flask_login import login_required

@app.route('/dashboard')
@login_required
def dashboard_html():
    return render_template('dashboard.html')






# -----------------------------------------------------------------------------
# Dev entrypoint ----------------------------------------------------------------
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Use 0.0.0.0 if you need LAN access; change port if 5000 collides.
    app.run(debug=True, host="127.0.0.1", port=5000)
