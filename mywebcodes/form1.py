from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def men():
    return render_template("form1.html")

@app.route("/hello",methods=["GET","POST"])
def xmen():
    if request.method=="GET":
        return "Please submit form"
    else:    
        name=request.form.get("name")
        return render_template("form2.html",name=name)
