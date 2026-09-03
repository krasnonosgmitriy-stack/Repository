from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.get_json()  # Отримуємо JSON з POST-запиту
    return jsonify({"message": "Дані отримано", "data": data})

if __name__ == '__main__':
    app.run(debug=True)