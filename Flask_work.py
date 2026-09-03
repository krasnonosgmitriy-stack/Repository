from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["SECRET_KEY"] = "my-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    password = db.Column(db.String(255),nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    text = db.Column(db.String(500),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)
    user = db.relationship("User",backref="comments")

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User,int(user_id))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user:
            return "є таке"

        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        return redirect(url_for("index"))
    return render_template("register_4.html")

@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user is None:
            return "знайдено"

        if not check_password_hash(user.password,password):
            return "neправильнa"
        login_user(user)

        return redirect(url_for("index"))

    return render_template("login_4.html")



@app.route("/create_coment",methods=["GET", "POST"])
@login_required
def create_coment():
    if request.method == "POST":
        text = request.form["text"]
        comment = Comment(text=text,user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for("comments"))
    return render_template("create_coment.html")

@app.route("/comments")
def comments():
    comments = Comment.query.order_by(Comment.id.desc()).all()
    return render_template("comments.html",comments=comments)
with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(debug=True)