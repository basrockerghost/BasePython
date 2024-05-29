import requests
import json
import random
import time

# ThingsBoard configuration
THINGSBOARD_HOST = 'a1a4f640-18d8-11ef-89bf-db5a56a39248'  # e.g., 'demo.thingsboard.io'
ACCESS_TOKEN = 'SexCqCMcvCR8fCkVpyP7'

url = "http://localhost:8080/api/v1/SexCqCMcvCR8fCkVpyP7/telemetry"

# Function to generate random telemetry data
def generate_random_telemetry():
    return {
        'temperature': random.uniform(20.0, 30.0),
        'humidity': random.uniform(30.0, 70.0),
        'pressure': random.uniform(1000, 1100)
    }

# Function to send telemetry data to ThingsBoard
def send_telemetry_data(data):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print('Data sent successfully:', data)
    else:
        print('Failed to send data:', response.status_code, response.text)

# Main loop to send data periodically
while True:
    telemetry_data = generate_random_telemetry()
    send_telemetry_data(telemetry_data)
    time.sleep(5)  # Send data every 5 seconds
