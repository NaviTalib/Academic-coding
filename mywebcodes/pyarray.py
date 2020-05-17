from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def pyarray():
    names = ["Talib","is","doing","BCA"]
    return render_template("listindext.html",names=names)