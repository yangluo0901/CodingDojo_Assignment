from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "Iwonttellyouthetruth"
mysql = MySQLConnector(app,"full_friends")
@app.route('/')
def index():
    query = "SELECT * FROM users"
    friends_list = mysql.query_db(query)
    return render_template("index.html", friends_list = friends_list)

@app.route('/add_friend', methods=['POST'])
def add():
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {
            "first_name" : request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email']
    }
    mysql.query_db(query,data)
    return redirect('/')

@app.route('/friends/<id>/edit',methods=['GET'])
def edit(id):
    return render_template("/edit.html",value =id)

@app.route('/friends/<id>',methods=['POST'])
def update(id):
    query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :id"
    data ={
            "first_name" : request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "id": id
    }
    mysql.query_db(query,data)
    return redirect('/')
@app.route('/friends/<id>/delete',methods=['POST'])
def delete(id):
    query = "DELETE FROM users WHERE id = :id"
    data = {
            'id': id
    }
    mysql.query_db(query,data)
    return redirect('/')
app.run(debug=True)
