from logging import debug
from flask import Flask, render_template  # Flask --> class , flask --> module 

app = Flask(__name__)
# here the __name__ --> is telling the space from where we need to find the 
# resources 
# flask_project --> pkg 
# Flask("flask_project")
# help(Flask)

# / --> ??
# /home/ --> ??
# /login/ --> ??

# let's do routing 

#@object.decorator_name(path)
@app.route("/")  # / --> domain(localhost for now) , route --> decorator
def index():
    # return "HELLO WORLD"
    return render_template("one.html")  # templates --> index.html
    # templates/index.html
    #eg -->  templates/htmlpages/index.html --> render_templates("htmlpages/index.html")

@app.route("/home/") # localhost/home/
def home():
    return "<h1 style='color:red'>WELCOME TO MY HOME OF PYTHON</h1>"

'''@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "PAGE NOT FOUND", 404'''

app.run(port=80, debug=True)
# debug = True --> show error on browser side
# development side --> means project is under development
# deployment side --> debug = False bcz we don't want to show our error to clients
