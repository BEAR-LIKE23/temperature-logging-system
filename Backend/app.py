from flask import Flask, render_template, jsonify, request
import json
import requests

app = Flask(__name__)

def load_temperature_data():
  try:
    with open('temperature_data.json', 'r') as f:
      return json.load(f)
  except FileNotFoundError:
    print("Temperature data file not found. Returning an empty list.")
    return []
  except json.JSONDecodeError:
    print("Error decoding JSON data from the file.")
    return []

@app.route('/')
def index():
  temperature_data = load_temperature_data()
  return render_template('index.html', temperature_data=temperature_data)

@app.route('/api/temperature_data', methods=['GET', 'POST'])
def temperature_data_endpoint():
  if request.method == 'GET':
    temperature_data = load_temperature_data()
    return jsonify(temperature_data)
  elif request.method == 'POST':
    # Get the data from the POST request
    new_data = request.get_json()

    # Load existing data from the file
    try:
      with open('temperature_data.json', 'r') as f:
        existing_data = json.load(f)
    except FileNotFoundError:
      existing_data = [] 

    # Ensure existing_data is a list (if it's a dictionary, make it a list)
    if not isinstance(existing_data, list):
      existing_data = [existing_data]

    # Append the new data to the list
    existing_data.append(new_data)

    # Save the updated data back to the file
    with open('temperature_data.json', 'w') as f:
      json.dump(existing_data, f)

    return jsonify({'message': 'Temperature data appended successfully'}), 201


if __name__ == '__main__':
  app.run(debug=True)
