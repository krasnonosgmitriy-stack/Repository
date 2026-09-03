from flask import Flask, render_template, request
from urllib.parse import quote
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qr_url = None
    text = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={quote(text)}"

    return render_template("QR_2.html", qr_url=qr_url, text=text)

if __name__ == "__main__":
    app.run(debug=True)