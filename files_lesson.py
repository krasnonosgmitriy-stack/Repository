from datetime import datetime
import uuid
import os
import uuid
import magic
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
FILE_PATH = "user_files2"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///files_2.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class File(db.Model):
    __tablename__ = "files"
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    file_desc = db.Column(db.String(510), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_file = request.files.get("user_file")
        file_desc = request.form.get("file_desc")

        mime = magic.Magic(mime=True)
        file_type = mime.from_buffer(user_file.read(1024))
        user_file.seek(0)

        if file_type not in ["image/png", "image/jpeg", "image/jpg"]:
            return "File unsupported type"

        if user_file.content_length >= 1024 * 1024 * 10:
            return "File larger than 10MB"

        filename = f"{uuid.uuid4()}_{user_file.filename}"
        file_path = os.path.join(FILE_PATH, filename)

        user_file.save(file_path)
        new_file = File(filename=filename, file_desc=file_desc)
        db.session.add(new_file)
        db.session.commit()
        return render_template(
            "first_page.html",
            message="Файл збережено"
        )
    else:
        return render_template("first_page.html")

@app.route("/gallery")
def gallery():
    files = File.query.order_by(File.date_created.desc()).all()
    return render_template("gallery.html", files=files)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)