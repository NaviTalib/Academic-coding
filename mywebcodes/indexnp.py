from flask import Flask,render_template

app=Flask(__name__)
@app.route("/")
def perv():
    return render_template("prevs.html")
@app.route("/more")
def next():
    return render_template("next.html")