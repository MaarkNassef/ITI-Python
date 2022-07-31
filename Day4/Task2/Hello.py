from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Home Page</h1>"

@app.route("/start")
def hello_start():
    return "<h1>Start Page</h1>"

@app.route("/AboutMe")
def hello_AboutMe():
    return open("m.html",'r').read(-1)