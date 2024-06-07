import csv
import requests

url = "http://localhost:8080/api/plugins/telemetry/DEVICE/a1a4f640-18d8-11ef-89bf-db5a56a39248/values/timeseries"
headers = {
    'Content-Type': 'application/json',
    'X-Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwidXNlcklkIjoiYjNhZTBiNTAtMThjMC0xMWVmLThmYTItMGZlNzYyOWRlNjBlIiwic2NvcGVzIjpbIlRFTkFOVF9BRE1JTiJdLCJzZXNzaW9uSWQiOiI5MTkyZDFkYy01YmYxLTRiNzEtYjdkYi04YmQxZjMyMGY4MWYiLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImlhdCI6MTcxNzc0MTQxNiwiZXhwIjoxNzE3NzUwNDE2LCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiYjM3N2I5MTAtMThjMC0xMWVmLThmYTItMGZlNzYyOWRlNjBlIiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCJ9.OEqTZKR8J9SF89UT_-_XE8sTr5i532kW4rmxQkMaVO8nwzZQa8U7FNjr7ca0EUVvQujVSpcO2b5bQFKxuJtXEQ'
}
params = {
    'keys': 'product_id,product_name,name,latitude,longitude,create_date,upload_date',
    'startTs': 1717693200000,
    'endTs': 1717779599000
}

# response = requests.get(url, headers=headers, params=params)
# data = response.json()

# with open('telemetry_data.csv', mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['timestamp', 'product_id', 'product_name', 'name', 'latitude', 'longitude', 'create_date', 'upload_date'])  # Write the header
    
#     for key, values in data.items():
#         for entry in values:
#             writer.writerow([entry['ts'], entry['value']])

response = requests.get(url, headers=headers, params=params)
data = response.json()

# Creating a dictionary to hold values for each timestamp
timestamp_data = {}

# Loop through the data and organize it by timestamp
for key, values in data.items():
    for entry in values:
        timestamp = entry['ts']
        if timestamp not in timestamp_data:
            timestamp_data[timestamp] = []
        timestamp_data[timestamp].append(entry['value'])

# Writing the organized data to CSV
with open('telemetry_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['timestamp'] + [f'product_id', 'product_name', 'name', 'latitude', 'longitude', 'create_date', 'upload_date'])  # Write the header
    
    for timestamp, values in timestamp_data.items():
        row = [timestamp] + values
        writer.writerow(row)