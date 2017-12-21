from flask import Flask, render_template,request,redirect,session,flash
import re
app = Flask(__name__)
app.secret_key = "thisisscret"
EMAIL_REGEX = re.compile('^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
UPPERCASE = re.compile('(?=.*[A-Z]).+$')
NUMERIC = re.compile('(?=.*[0-9]).+$')
@app.route("/")
def login():
    return render_template("form_validation.html")
    print "1"

@app.route("/registration", methods=["POST"])
def register():
    error = False
    if len(request.form["first_name"]) == 0:
        flash("First name cannnot be empty!")
        error = True
        print "2"
    if len(request.form["last_name"]) == 0:
        flash("Last name cannot be empty!")
        error = True
    if request.form["first_name"].isalpha() is False or request.form["last_name"].isalpha() is False:
        flash("Name cannot contain numbers!")
        error = True
    if len(request.form["email"]) == 0:
        flash("Email cannot be empty!")
        error = True
        print "3"
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid e-mail address!")
        error = True
        print "4"
    if len (request.form["password"]) == 0:
        flash ("Password needed !")
    elif len(request.form["password"]) < 8:
        flash("Password cannot be less than 8 characters!")
        error = True
    elif not UPPERCASE.match(request.form["password"]):
    # elif request.form["password"].islower():
        flash("Password at least has one uppercase letter!")
        error = True
        print "1111"
    elif not NUMERIC.match(request.form["password"]):
    # elif request.form["password"].isalpha():
        flash("Password must has at least one number!")
        error = True
    if request.form["password"] != request.form["c_password"]:
        flash("Passwords dont match!")
        error = True
        print "5"
    if error  == True:
        return redirect("/")
        print "6"
    print "7"
    return render_template("success.html")


app.run(debug=True)
