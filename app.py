from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))

    user = cur.fetchone()

    conn.close()

    if user:
        return redirect("/dashboard")
    else:
        return "Login Failed"


@app.route("/register")
def register_page():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO users(username,password) VALUES(?,?)",(username,password))

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


app.run(debug=True)
