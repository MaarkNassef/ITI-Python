from unicodedata import name
from flask import redirect, request, url_for
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>', methods=['GET','POST'])
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/register', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('hello',name=username))
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')