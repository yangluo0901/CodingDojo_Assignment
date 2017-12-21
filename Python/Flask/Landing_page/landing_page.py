from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def function1():
	return render_template("index.html")


@app.route("/ninjas")
def function2():
    return render_template("ninja.html")

@app.route("/dojos/new")
def function3():
	return render_template("dojos.html")
app.run(debug=True)
