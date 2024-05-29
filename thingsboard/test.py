import requests
import json
import random
import time

THINGSBOARD_HOST = 'a1a4f640-18d8-11ef-89bf-db5a56a39248'  # e.g., 'demo.thingsboard.io'
ACCESS_TOKEN = 'SexCqCMcvCR8fCkVpyP7'

url = "http://localhost:8080/api/v1/SexCqCMcvCR8fCkVpyP7/telemetry"
headers = {
    "Content-Type": "application/json"
}

# data = {
    
# }

def pullProductName() :
    product = [["1", "Bread", 34.6777116, 135.403636, "คุณ A"], ["2", "Snack", 34.6777116, 135.403636, "คุณ B"], ["3", "M&M", 35.6684103, 139.5760574, "คุณ C"], ["4", "Chocolate", 33.5598967, 130.355533, "คุณ D"], ["5", "huh", 35.634426, 139.3485075, "คุณ E"]]
    randomProduct = random.choice(product)
    return {"product_id" : randomProduct[0], "product_name" : randomProduct[1], "latitude" : randomProduct[2], "longitude" : randomProduct[3], "name" : randomProduct[4]}
 


# response = requests.post(url, headers=headers, data=json.dumps(data))
# print(response.status_code)
# print(response.text)
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
    telemetry_data = pullProductName()
    send_telemetry_data(telemetry_data)
    time.sleep(5)  # Send data every 5 seconds
