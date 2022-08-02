from flask import Flask, redirect, render_template,request, url_for
import sqlite3
import create_db
app = Flask(__name__)
@app.route("/")
def index():
    conn = sqlite3.connect('my_db.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Student")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    return render_template("index.html",rows = rows)

@app.route("/addStudent", methods=['GET','POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        create_db.add_student_db(name,int(age),city)
        return redirect(url_for('index'))
    return render_template("add_students.html")

@app.route("/Search", methods=['GET','POST'])
def search(rows=None):
    if request.method == 'POST':
        search = request.form['search']
        conn = sqlite3.connect('my_db.sqlite')
        cur = conn.cursor()
        query = f"SELECT * FROM Student WHERE LOWER(username) LIKE LOWER('%{search}%') OR LOWER(city) LIKE LOWER('%{search}%');"
        cur.execute(query)
        rows = cur.fetchall()
        if len(rows) == 0:
            rows = None
    return render_template("search.html",rows=rows)