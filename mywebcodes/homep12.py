from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def one():
    return render_template("page1.html")

@app.route("/next")
def two():
    return render_template("page2.html")