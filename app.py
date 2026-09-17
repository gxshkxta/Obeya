import os
from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "obeya-secret-key-12345")

# Четем позволените имейли от .env или задаваме дефолтни
ALLOWED_EMAILS = [e.strip() for e in os.getenv("ALLOWED_EMAILS", "kinetrix.support@gmail.com").split(",")]
APP_PASSWORD = os.getenv("APP_PASSWORD", "3mYbs")

@app.route("/")
def index():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    # Подаваме правилните речници/структури, които HTML шаблонът очаква
    return render_template(
        "board.html",
        user_email=session.get("user_email"),
        statuses={"todo": "За изпълнение", "in_progress": "В процес", "done": "Готови"},
        tasks=[],
        decisions=[],
        ideas=[],
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()
        
        if email in ALLOWED_EMAILS and password == APP_PASSWORD:
            session["logged_in"] = True
            session["user_email"] = email
            return redirect(url_for("index"))
        else:
            error = "Грешен имейл или парола! Опитай отново."
            
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/board")
def board():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("board.html", user_email=session.get("user_email"), statuses=[], tasks=[], decisions=[], ideas=[])

@app.route("/decisions")
def decisions():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("decisions.html", user_email=session.get("user_email"))

@app.route("/ideas")
def ideas():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("ideas.html", user_email=session.get("user_email"))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
