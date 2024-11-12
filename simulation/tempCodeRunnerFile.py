import random
import time
import requests
import json


def generate_temperature():
    return round(random.uniform(20.0, 30.0), 2)


def send_data_to_server(temp):
    url = "http://localhost:5000  # Simulated API endpoint
    data = {"temperature": temp, "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}
    try:
        response = requests.post(url, json=data)
        print(f"Server Response: {response.status_code}, {response.text}")

        # Save the data to the temperature_data.json file
        save_data_to_file(data)
    except Exception as e:
        print(f"Error sending data: {e}")


def save_data_to_file(data):
    with open("temperature_data.json", "a") as f:
        # Append the data to the file in JSON format, separated by newline
        f.write(json.dumps(data) + "\n")
        print("saved new data")


# Simulate sending temperature data every 10 seconds
while True:
    temp = generate_temperature()
    print(f"Simulated Temperature: {temp}°C")
    send_data_to_server(temp)
    time.sleep(10)
