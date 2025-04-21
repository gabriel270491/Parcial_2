
from flask import Flask, jsonify
import json

app = Flask(__name__)

with open('data.json', 'r') as f:
    data = json.load(f)

@app.route('/api/v1/vacunacion', methods=['GET'])
def get_all_data():
    return jsonify(data)

@app.route('/api/v1/vacunacion/anio/<int:year>', methods=['GET'])
def get_by_year(year):
    result = [entry for entry in data if entry['year'] == year]
    return jsonify(result)

@app.route('/api/v1/vacunacion/provincia/<string:province>', methods=['GET'])
def get_by_province(province):
    result = [entry for entry in data if entry['province'].lower() == province.lower()]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
