from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>whats up</h1>"

@app.route("/fun")
def fun():
    return "yes"
    
@app.route("/func")
def func():
    return "yes yes"        
