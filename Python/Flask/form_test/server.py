from flask import Flask, render_template, request, redirect, session,flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route("/")

def index():
  return render_template("index.html")

@app.route("/users",methods=["POST"])
def create_users():
    if len(request.form["name"])<1:
        flash("Name cannot be empty!")
    else:
        flash("Success! Your name is {}".format(request.form["name"]))
        session["name"] = request.form["name"]
        session["email"] = request.form["email"]
    return redirect("/show")


@app.route("/show")
def show_users():
    try:
        return render_template("result.html",name=session["name"],email= session["email"])
    except:
        session["name"]="none"
        session["email"]="none"
        return render_template("result.html",name=session["name"],email= session["email"])


@app.route("/reset")
def reset():
    session.pop("name")
    session.pop("email")
    return redirect("/")
app.run(debug=True)
