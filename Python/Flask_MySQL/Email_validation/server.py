from flask import Flask,request,render_template,redirect,flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'secret!'
mysql = MySQLConnector(app,"email_validation")
EMAIL_REGEX = re.compile('^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/validation', methods=['POST'])
def validate():
    show = False
    if len(request.form['email']) < 1:
        flash('The E-mail cannot be blank!')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('E-mail is not valid!')
    else:
        flash('Success!')
        show = True
        query1 = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email,NOW(),NOW())"
        data = {
                'email' : request.form['email']
        }
        mysql.query_db(query1,data)
        query2 = "SELECT * FROM emails"
        emails = mysql.query_db(query2)
        print emails
    return render_template('index.html',all_emails = emails,show =show )

@app.route('/delete',methods=['POST'])
def delete():
    query3 = "DELETE FROM emails WHERE email = :defined_email"
    data3 = {
            'defined_email': request.form['email']
            }
    mysql.query_db(query3,data3)
    query2 = "SELECT * FROM emails"
    emails = mysql.query_db(query2)
    print emails
    return render_template('index.html',all_emails = emails,show =True )

app.run(debug = True)
