import random
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def random2():
    return f"Hellon, World:{random.randint(1,100)}"

@app.route("/index")
@app.route("/golovna")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about_updated.html")

@app.route("/contact")
def contact():
    return render_template("contact_updated.html")

@app.route("/mesto")
def misto():
    return render_template("mesto.html")

@app.route("/user/<name>")
def hellop(name):
    return f"Hello, {name}!"

def suma(number1, number2):
    return f"Your suma is {number1+number2}"

if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0", port=8080)