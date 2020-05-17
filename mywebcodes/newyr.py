from flask import Flask,render_template
import datetime

app=Flask(__name__)

@app.route("/")
def fun():
    now=datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("newyr.html",new_year=new_year)