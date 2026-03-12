from flask import Flask,render_template,request,redirect,session,jsonify
from database.models import init_db
from database.db import get_db

from modules.ip_lookup import lookup as ip_lookup
from modules.domain_lookup import lookup as domain_lookup
from modules.username_lookup import lookup as username_lookup

app = Flask(__name__)
app.secret_key="osint_secret"

init_db()

@app.route("/")
def home():

    if "user" in session:
        return redirect("/dashboard")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/")

    return render_template("dashboard.html")


@app.route("/ip_lookup",methods=["POST"])
def ip_tool():

    ip=request.form["ip"]

    data=ip_lookup(ip)

    return jsonify(data)


@app.route("/domain_lookup",methods=["POST"])
def domain_tool():

    domain=request.form["domain"]

    data=domain_lookup(domain)

    return jsonify(str(data))


@app.route("/username_lookup",methods=["POST"])
def username_tool():

    username=request.form["username"]

    data=username_lookup(username)

    return jsonify(data)


app.run(debug=True)
