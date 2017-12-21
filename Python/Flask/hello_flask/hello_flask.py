from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def function():
    return render_template("index.html", name = "hahaha")
app.run(debug=True)
