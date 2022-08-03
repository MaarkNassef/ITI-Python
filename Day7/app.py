from flask import Flask, redirect, render_template,request, url_for
import sqlite3
import db
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

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    if request.method == 'POST':
        connect_db = db.get_db()
        connect_db.execute(f"UPDATE Student SET username = '{request.form['name']}', age = '{request.form['age']}', city = '{request.form['city']}' WHERE id = {id};")
        connect_db.commit()
        db.close_db(connect_db)
        return redirect(url_for('index'))
    conn = sqlite3.connect('my_db.sqlite')
    cur = conn.cursor()
    query = f"SELECT * FROM Student WHERE id = {id};"
    cur.execute(query)
    row = cur.fetchone()
    return render_template('update.html', row=row)

@app.route('/delete/<int:id>')
def delete(id):
    connect_db = db.get_db()
    connect_db.execute(f"DELETE FROM Student WHERE id = {id};")
    connect_db.commit()
    db.close_db(connect_db)
    return redirect(url_for('index'))