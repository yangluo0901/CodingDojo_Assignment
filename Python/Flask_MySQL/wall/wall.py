from flask import Flask, render_template, session, request, flash, redirect,url_for
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "lalalala"
mysql = MySQLConnector(app,"wall")
@app.route('/') # login page
def login_page():
     return render_template("index.html")

@app.route('/registration_page', methods = ["POST"]) # register page
def registration_page():
    return render_template("registration.html")


@app.route('/registration_page/register', methods=['POST']) # register handling
def register():
    password_confirmation = request.form['password_confirmation']
    password = request.form['password']
    if password == password_confirmation:
        pw_hash = bcrypt.generate_password_hash(password)
        query_register = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES(:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        data_register = {
                        'first_name': request.form['first_name'],
                        'last_name': request.form['last_name'],
                        'email': request.form['email'],
                        'pw_hash': pw_hash
        }
        mysql.query_db(query_register,data_register)
        return redirect('/')
    else:
        flash("Passwords do not match !")
        return render_template("registration.html")

@app.route('/wall')#wall page
def wall():
    query_messages = "SELECT GROUP_CONCAT(first_name,last_name) AS name,message,messages.id as message_id,messages.created_at FROM messages JOIN users ON messages.user_id = users.id GROUP BY messages.id"

    all_messages = mysql.query_db(query_messages)

    query_comment = """SELECT messages.id, message, messages.user_id as message_user_id, comment, comments.user_id as comment_user_id, concat(first_name, users.last_name)as name,comments.created_at as time FROM messages
                        JOIN comments ON messages.id = comments.message_id
                        join users on comments.user_id = users.id"""
    all_message_comment = mysql.query_db(query_comment)
    print all_message_comment[0]['time']
    return render_template("wall.html", all_messages = all_messages, all_message_comment = all_message_comment)

@app.route('/login', methods=["POST"]) # handle login
def login():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    query_login = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data_login = {
                'email': email
    }
    user = mysql.query_db(query_login,data_login)
    if len(user)>0:
        session["user_id"]= user[0]['id']
        if bcrypt.check_password_hash(user[0]['pw_hash'], password):
            flash("Successfully!")
            return redirect('/wall')
        else:
            flash(" Wrong password !")
            return redirect('/')
    else:
        flash(" Invalid E-mail !")
    return redirect('/')

@app.route('/post_messages', methods=['POST'])# post message process
def message():
    message = request.form['message']
    query_post_message = "INSERT INTO  messages (message,user_id, created_at,updated_at) VALUES (:message,:user_id, NOW(),NOW())"
    data = {
            'message':message,
            'user_id':int(session['user_id'])
    }

    mysql.query_db(query_post_message,data)
    return redirect('/wall')

@app.route('/post_comment/<message_id>', methods=['POST'])
def comment(message_id):
    comment = request.form['comment']
    if len(comment)>0:
        query_comment = "INSERT INTO comments (comment,user_id,message_id,created_at,updated_at) VALUES (:comment,:user_id,:message_id,NOW(), NOW())"
        data_comment = {
                    'comment': comment,
                    'user_id':int(session['user_id']),
                    'message_id':int(message_id)
        }
        mysql.query_db(query_comment,data_comment)
    return redirect('/wall')


app.run(debug=True)
