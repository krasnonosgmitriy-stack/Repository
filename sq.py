import sqlite3

from flask import Flask, g, render_template, request

DATABASE = 'students.db'

app = Flask(__name__)

def connect_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS user ("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "name TEXT NOT NULL,"
                   "email TEXT UNIQUE NOT NULL,"
                   "city TEXT NOT NULL,"
                   "country TEXT NOT NULL,"
                   "phone INTEGER NOT NULL)")
    db.commit()

@app.route('/')
def index():
    return render_template("index_db.html")

@app.route('/join', methods=['POST', 'GET'])
def join():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        city = request.form.get('city')
        country = request.form.get('country')
        phone = request.form.get('phone')
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("""INSERT INTO user (name, email, city, country, phone) VALUES (?, ?, ?, ?, ?)""",
                       (name, email, city, country, phone))
        db.commit()
    return render_template("join_db.html")

@app.route('/users')
def participants():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()
    return render_template("users_db.html", data=data)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)