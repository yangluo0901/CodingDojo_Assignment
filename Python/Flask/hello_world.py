from flask import Flask
app = Flask(__name__)

@app.route("/")

def function():
    return  "helllo world!"
app.run(debug=True)
