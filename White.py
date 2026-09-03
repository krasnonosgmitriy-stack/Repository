import requests
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta, timezone

Kyiv_timezone = timezone(timedelta(hours=4))
Kyiv_time = datetime.now(Kyiv_timezone)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(30), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=Kyiv_time)

    def to_dictk(self):
        return {'id': self.id, 'city': self.city, 'temperature': self.temperature, 'created_at': self.created_at}
with app.app_context():
    db.create_all()

@app.route('/weather/<city>')
def weather(city):
    url = f'http://wttr.in/{city}?format=j1'
    response = requests.get(url)
    if response.status_code == 200:
        result = jsonify({"error": "Not found"}), 404
    data = response.json()
    current = data['current_condition'][0]
    temperature = current['temp_C']
    record = Weather(city=city, temperature=temperature)
    db.session.add(record)
    db.session.commit()
    return jsonify(record.to_dictk())

@app.route("/all_records")
def all_records():
    records = Weather.query.all()
    return render_template('all_records.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)

