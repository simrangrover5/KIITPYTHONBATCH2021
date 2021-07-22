from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("one.html")

@app.route("/name/<name_>/<int:age>/")  # localhost/name/simran/12
def get_name(name_, age):
    return render_template("one.html", name=name_, a=age)
    # return f"<h1 style='color:coral'>Welcome {name_} of age {age}</h1>"

@app.route("/<name>/<int:m1>/<int:m2>/<int:m3>/")
def details(name, m1, m2, m3):
    data = {
        "Name" : name, 
        "Maths" : m1,
        "Science": m2,
        "English": m3
    }
    return render_template("one.html", data=data)

app.run(debug=True) # host --> localhost, port --> 5000

# localhost/name/simran --> Welcome simran
# localhost/name/manish --> Welcome manish
# localhost/name/tushar --> Welcome tushar
#<variable> --> data type --> string, <int:a>, <float:a>