from flask import Flask, render_template,request,redirect,flash,session

app = Flask(__name__)
app.secret_key="this is secret"
@app.route("/")
def form():
    return render_template("form.html")

@app.route("/users", methods=["POST"])
def submit():
    if len(request.form["name"])<1:
        flash("Name Cannot be Empty!")
        print "111111111"
    if len(request.form["comment"])<1:
        flash("Comment Cannot be Empty !")
        print "22222222"
    if len(request.form["comment"])>120:
        flash(" Comment exceeds limits !")
        print "33333333"
    else:
        name = request.form['name']
        location = request.form['Dojo Location']
        language = request.form['favorite language']
        comment = request.form['comment']
        print name
        return render_template("submitted_info.html", name=name,location=location,language=language,comment=comment)
    return redirect("/")
app.run(debug=True)
# how to achieve this message by "alert"?
