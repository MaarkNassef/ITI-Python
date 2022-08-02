from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/start/<name>/<num>")
def hello_name(name,num):
    return f"<p>Hello, {name}!</p>"*int(num)

@app.route("/<name>")
def injection(name):
    return f"<p>Hello, {name}!</p>"

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)