from flask import Flask, render_template,request,redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():
    if 'target' not in session:
        session["target"]=random.randint(1,100)
    return render_template("index.html")

@app.route("/guess",methods=["POST"])
def game():
    session["guess"]=int(request.form["number"])
    if session["target"] > session["guess"]:
        session["result"]="low"
    elif session["target"] <  session["guess"] :
        session["result"]="high"
    else:
        session["result"]="Bingo"
    return redirect("/")

@app.route("/reset",methods=["POST","GET"])
def reset():
    session.pop("target")
    session.pop("guess")
    session.pop("result")
    return redirect("/")

app.run(debug=True)
