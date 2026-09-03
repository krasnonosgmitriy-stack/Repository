from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    __tablename__ = 'films'
    def __repr__(self):
        return '<Film %r>' % self.username

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        description = request.form['description']
        newfilm = Film(username=username, description=description)
        db.session.add(newfilm)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('form.html')

@app.route('/users')
def users():
    all_films = Film.query.all()
    return render_template('users.html', films=all_films)

if __name__ == "__main__":
    app.run(debug=True)