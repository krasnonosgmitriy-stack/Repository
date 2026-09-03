from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager,login_user,login_required,logout_user,current_user
from online_magazin_db import db, Users, Menu, Orders, Reservation

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///online_restaurant.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Users, int(user_id))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = Users.query.filter_by(username=username).first()
        if user:
            flash("є такий користувач")
            return redirect(url_for("register"))
        new_user = Users(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash("успішна")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = Users.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash("ви увійшли")
            return redirect(url_for("index"))
        flash("неправильна")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("успішно вийшов")
    return redirect(url_for("index"))


@app.route("/create_menu", methods=["GET", "POST"])
@login_required
def create_menu():
    if menu.query.first():
        return "menu вже є"
    menu_456 = [Menu(name="Піца Маргарита",description="Томатний соус, сир моцарела та базилік",price=250),
        Menu(name="Бургер",description="Соковита котлета, сир, овочі та соус",price=180),
        Menu(name="Паста Карбонара",description="Паста з беконом у вершковому соусі",price=220),
        Menu(name="Цезар",description="Курка, салат, помідори, сир та соус",price=170)]
    db.session.add_all(menu_456)
    db.session.commit()
    return "Меню успішно додано!"

@app.route("/menu")
def menu():
    menu_items = Menu.query.all()
    return render_template("menu.html", menu_items=menu_items)

@app.route("/order/<int:menu_id>", methods=["GET", "POST"])
@login_required
def order(menu_id):
    menu_item = db.session.get(Menu, menu_id)
    if not menu_item:
        return "не знаю такого", 404
    if request.method == "POST":
        quantity = int(request.form.get("quantity", 1))
        new_order = Orders(user_id=current_user.id, menu_id=menu_id, quantity=quantity)
        db.session.add(new_order)
        db.session.commit()
        flash("є замовлення")
        return redirect(url_for("menu"))
    return render_template("order.html", menu_item=menu_item)

