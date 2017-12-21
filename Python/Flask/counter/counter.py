from flask import Flask, render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def counter():
    try:
        session["times"] += 1
    except:
        session["times"] = 1

    return render_template("counter.html",times=session["times"])

@app.route("/ninjas",methods=['POST','GET'])
def ninja():
    session["times"] += 1
    return redirect("/")



@app.route("/reset", methods=['POST','GET'])
def reset():
    print "hello"
    session['times'] = 0
    return redirect("/")

app.run(debug=True)
