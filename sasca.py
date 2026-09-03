from flask import Flask, render_template

app = Flask(__name__)


students = [
    {"name": "Vlad", "score": 100},
    {"name": "Sviatoslav", "score": 99},
    {"name": "Юстин", "score": 100},
    {"name": "Viktor", "score": 79},
    {"name": "Ярослав", "score": 93}
]
max_score = 100

@app.route('/results')
def results():
    return render_template("дневник.html", students=students, max_score=max_score)

@app.route('/<name>')
def student_name(name):
    return render_template("username.html", name=name, students=students)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')