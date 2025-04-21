from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Cargar datos desde un archivo JSON simulado
with open('data.json', 'r') as f:
    vaccination_data = json.load(f)

@app.route('/api/v1/vacunacion', methods=['GET'])
def get_all_data():
    return jsonify(vaccination_data)

@app.route('/api/v1/vacunacion/anio/<int:year>', methods=['GET'])
def get_data_by_year(year):
    result = [entry for entry in vaccination_data if entry['year'] == year]
    return jsonify(result)

@app.route('/api/v1/vacunacion/provincia/<provincia>', methods=['GET'])
def get_data_by_provincia(provincia):
    result = [entry for entry in vaccination_data if entry['province'].lower() == provincia.lower()]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
