from flask import Flask, render_template,request,redirect,session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route("/")
def index():
    if "gold" not in session:
        session["gold"]=0
        session["activities"]=[];
    return render_template("ninja_gold.html")

@app.route("/process_money",methods=["POST","GET"])
def process_money():
    time =  datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    if request.form["location"] == "farm":
        gold= random.randint(10,20)
        session["activities"].append({'history': "You entered a {} and earned {} golds".format(request.form["location"], gold),'class': '', 'date':time})
    elif request.form["location"] == "cave":
        gold = random.randint(5,10)
        session["activities"].append({'history': "You entered a {} and earned {} golds".format(request.form["location"], gold),'class': '', 'date':time})
    elif request.form["location"] == "house":
        gold = random.randint(2,5)
        session['activities'].append({'history': "You entered a {} and earned {} golds".format(request.form["location"], gold),'class': '', 'date':time})
    elif request.form["location"] == "casino":
        gold = random.randint(0,50)
        if random.randint(0,1)==0:
            weigh = 1
            session['activities'].append({'history': "You entered a {} and earned {} golds".format(request.form["location"], gold),'class': '', 'date':time})
        else:
            weigh = -1
            session['activities'].append({'history': "You entered a {} and lost {} golds ... Ouch ...".format(request.form["location"], gold), 'class': 'loss', 'date':time})
        gold = gold * weigh

    session["gold"]+=gold
    print session["activities"]
    print gold
    return redirect("/")

@app.route("/reset")
def reset():
    session.pop("gold")

    return redirect("/")
app.run(debug=True)

# # REALLY IMPORTANT!!!!!!!!
# After pressing submit button twice, the session["activities"] is
# [{u'date': '2017-11-14 06:19:36 PM', u'class': '', u'history': 'You entered a farm and earned 14 golds'},
# {'date': '2017-11-14 06:20:18 PM', 'class': 'loss', 'history': 'You entered a casino and lost 13 golds ... Ouch ...'}]
# --> session["key"] is more like "List", that might be why we can use "append" method to session["key"]
# We can also assume that session exists as {"activities":[{"history":...., "class":.... },{"history":+++++, "class":+++}]
#                                             "gold":[{"":......," ":.....},{" ":......, " ":.......}]
#                                             }
# session is object, and session[" "] is list that contains couple of objects
#
