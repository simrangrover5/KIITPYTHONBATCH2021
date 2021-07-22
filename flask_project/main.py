from logging import debug
from flask import Flask, request
from flask.templating import render_template 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("nav.html")

@app.route("/register/") # localhost/register/
def register():
    return render_template("register.html")

@app.route("/afterregister/", methods=['GET', 'POST'])
def afterregister():
    if request.method == "GET":
        return render_template("register.html")
    else: 
        name = request.form.get("fname")  # {"fname":value, "email":email, 'passwd':p}
        email = request.form.get("email")
        passwd = request.form.get("passwd")
        return f"{name} --> {email} --> {passwd}"
app.run(port=80, debug=True)