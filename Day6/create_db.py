from db import get_db, close_db
def create_tables():
    connect_db = get_db()
    connect_db.execute("""CREATE TABLE Student (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        age TEXT NOT NULL,
                        city TEXT
                        );""")
    connect_db.commit()
    close_db()

def add_student_db(student_name,age,city):
    connect_db = get_db()
    connect_db.execute(f"INSERT INTO Student(username,age,city) VALUES('{student_name}',{age},'{city}');")
    connect_db.commit()
    close_db(connect_db)