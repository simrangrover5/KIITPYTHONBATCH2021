from logging import debug
from flask import Flask, request, redirect, url_for, make_response, session
from flask.templating import render_template 
import pymysql as sql 

app = Flask(__name__)
app.secret_key = "1234oiygihwef7890anhjkioplgfryikjlo"

def db_connect():
    db = sql.connect(host="localhost", port=3306, user="root", password="", 
                    database="kiitbatch")
    cursor = db.cursor()
    return db, cursor 

@app.route("/")
def index():
    if request.cookies.get("islogin"): # user already logged in 
        return render_template("afterlogin.html")
    return render_template("nav.html")

@app.route("/register/") # localhost/register/
def register():
    if request.cookies.get("islogin"):
        return render_template("afterlogin.html")
    return render_template("register.html")

@app.route("/afterregister/", methods=['GET', 'POST'])
def afterregister():
    if request.method == "GET":
        return render_template("register.html")
    else: 
        name = request.form.get("fname")  # {"fname":value, "email":email, 'passwd':p}
        email = request.form.get("email")
        passwd = request.form.get("passwd")
        db, cursor = db_connect()
        cmd = f"select email from users where email='{email}'"
        cursor.execute(cmd)
        data = cursor.fetchone() # will get email is user exists else get None
        if data: # user already exists
            msg = "Email Already Exists"
            return render_template("register.html", msg=msg)
        else: # no user already exists 
            cmd = f"insert into users values('{name}', '{email}', '{passwd}')"
            cursor.execute(cmd)
            db.commit()
            msg = 'Register Successfully.'
            return render_template("login.html", msg=msg)

@app.route("/signin/")
def signin():
    return render_template("login.html")

@app.route("/afterlogin/", methods=['GET', 'POST'])
def afterlogin():
    if request.method == "GET":
        return redirect(url_for("signin")) # redirect the request to the url at which signin function is running 
    else:
        email = request.form.get("email")
        passwd = request.form.get("passwd")
        db, cursor = db_connect()
        cmd =f"select * from users where email='{email}' and password='{passwd}'"
        cursor.execute(cmd)
        data = cursor.fetchone()
        if data: # user exists
            # resp = make_response(render_template("afterlogin.html")) # to set cookie 
            # resp.set_cookie('email', email)
            # resp.set_cookie("islogin", 'true')
            # return resp 
            session['email'] = email 
            session['islogin'] = 'true'
            return render_template("afterlogin.html")
        else: # user does not exists
            msg = "Invalid Email Id or Password"
            return render_template("login.html", msg=msg)

@app.route("/logout/")
def logout():
    del session['email']
    del session['islogin']
    return redirect(url_for("index"))
    # resp = make_response(render_template("nav.html"))  # we are creating this object to delete cookie from it
    # resp.delete_cookie("email")
    # resp.delete_cookie("islogin")
    # return resp
app.run(port=80, debug=True)

# when you are registering the data then you need to validate the password
# if password is validated then store the password in database after encyrpting it
# passlib or cryptgraphy