from flask import Flask, jsonify, render_template
from flask_caching import Cache
import time
import logging
import os
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
os.makedirs("logs", exist_ok=True)
handler = RotatingFileHandler("logs/app.log",maxBytes=100_000,backupCount=3)
handler.setLevel(logging.WARNING)
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
app.logger.addHandler(handler)
app.config["CACHE_TYPE"] = "SimpleCache"
app.config["CACHE_DEFAULT_TIMEOUT"] = 300
cache = Cache(app)

@app.route("/")
def index():
    return render_template("caching.html")

@app.route("/order")
def order():
    app.logger.warning("Товару немає")
    return jsonify({"message": "Помилку записано в лог","status": "warning"})

@app.route("/heavy-page")
@cache.cached(timeout=10)
def heavy_page():
    time.sleep(5)
    return jsonify({"message": "Це важка сторінка","generated_at": time.time()})

@cache.memoize(timeout=30)
def calculate(number):
    time.sleep(5)
    return number * number

@app.route("/calculate/<int:number>")
def calculation(number):
    result = calculate(number)
    return jsonify({"number": number,"result": result})


if __name__ == "__main__":
    app.run(debug=True)