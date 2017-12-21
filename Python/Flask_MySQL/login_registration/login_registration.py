from flask import Flask, render_template, session, request, flash, redirect
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
email_regex = re.compile('^[0-9a-zA-Z\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "Iwonttellyou"
mysql = MySQLConnector(app,"login_registration")

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login', methods = ['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    query_login = " SELECT * FROM users WHERE email = :email LIMIT 1"
    data_login = {
                "email":email
    }
    user = mysql.query_db(query_login,data_login)
    if user[0]:
        if bcrypt.check_password_hash(user[0]['pw_hash'],password):
            return redirect('/')
        else:
            flash("Wrong Password !")
    else:
        flash("Invalid E-mail !")

@app.route('/registration', methods = ["POST"])
def registration_page():
    return render_template("registration.html")


@app.route('/registration_page/register', methods = ['POST'])
def registration():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']

    if len(first_name) < 3:
        flash(" First Name Cannot Be Less Than 2!")
    elif first_name.isalpha() is False:
        flash("First Name Should Not Contain Numbers!")
    if len(last_name) < 3:
        flash(" Last Name Cannot Be Less Than 2!")
    elif last_name.isalpha() is False:
        flash("First Name Should Not Contain Numbers!")
    if len(email) == 0:
        flash("E-mail Cannot Be Empty!")
    elif not email_regex.match(email):
        flash("Email Not Valid!")
    if len(password) < 9:
        flash("Password Should Be At Least 8 Characters!")
    if password != password_confirmation:
        Flash(" Two Passwards You Input Do Not Match!")
    else:
        pw_hash = bcrypt.generate_password_hash(password)
        query_register = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES(:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        data_register = {
                        'first_name': request.form['first_name'],
                        'last_name': request.form['last_name'],
                        'email': request.form['email'],
                        'pw_hash': pw_hash
        }
        mysql.query_db(query_register,data_register)
        query_list = "SELECT * FROM users"
        user_list = mysql.query_db(query_list)
        return render_template("list.html",user_list = user_list)



app.run(debug = True)
