import random
import time
import requests

def generate_temperature():
    return round(random.uniform(20.0, 30.0), 2)

def send_data_to_server(temp):
    url = "http://localhost:5000/api/temperature"  # Simulated API endpoint
    data = {
        "temperature": temp,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        response = requests.post(url, json=data)
        print(f"Server Response: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error sending data: {e}")

# Simulate sending temperature data every 60 seconds
while True:
    temp = generate_temperature()
    print(f"Simulated Temperature: {temp}°C")
    send_data_to_server(temp)
    time.sleep(10)
