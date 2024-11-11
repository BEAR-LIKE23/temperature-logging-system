from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load temperature data from the JSON file (or create a sample)
def load_temperature_data():
    with open('temperature_data.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    # Fetch temperature data and pass it to the HTML template
    temperature_data = load_temperature_data()
    return render_template('index.html', temperature_data=temperature_data)

@app.route('/api/temperature')
def get_temperature_data():
    # Return temperature data as JSON
    temperature_data = load_temperature_data()
    return jsonify(temperature_data)

if __name__ == '__main__':
    app.run(debug=True)
