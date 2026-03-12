
from flask import Flask,render_template,request,redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS searches(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search",methods=["POST"])
def search():

    query=request.form["query"]

    conn=sqlite3.connect("database.db")
    cur=conn.cursor()

    cur.execute("INSERT INTO searches(query) VALUES(?)",(query,))
    conn.commit()
    conn.close()

    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():

    conn=sqlite3.connect("database.db")
    cur=conn.cursor()

    cur.execute("SELECT * FROM searches")
    data=cur.fetchall()

    conn.close()

    return render_template("dashboard.html",data=data)

app.run(debug=True)
