from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "hello, world !"

@app.route("/<string:name>")
def hlw(name):
   # name=name.capitalization()
    return f"hello,<h1>{name}</h1>"
