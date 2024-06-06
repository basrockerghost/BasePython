import csv
import requests

url = "http://localhost:8080/api/plugins/telemetry/DEVICE/a1a4f640-18d8-11ef-89bf-db5a56a39248/values/timeseries"
headers = {
    'Content-Type': 'application/json',
    'X-Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwidXNlcklkIjoiYjNhZTBiNTAtMThjMC0xMWVmLThmYTItMGZlNzYyOWRlNjBlIiwic2NvcGVzIjpbIlRFTkFOVF9BRE1JTiJdLCJzZXNzaW9uSWQiOiI5MDU3ODk3Yi1kYzhjLTRjZjAtOTgyMC1iYjg1MmM4ODlhM2EiLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImlhdCI6MTcxNzY0NjA4MiwiZXhwIjoxNzE3NjU1MDgyLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiYjM3N2I5MTAtMThjMC0xMWVmLThmYTItMGZlNzYyOWRlNjBlIiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCJ9.p6geRiJ8lgDs2zUDGDYD-T_5frESwmjGXLYYA7eE1Sq5rjNNPQ23H1Ma6q5HWNJnzRVHx7ibRAmtGMGAWVu9Vg'
}
params = {
    'keys': 'product_id, product_name',
    'startTs': 1579735870785,
    'endTs': 1717637830632
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

with open('telemetry_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['timestamp', 'key1', 'value1', 'key2', 'value2'])  # Write the header

    for keys, values in data.items():
        for entry in values:
            writer.writerow([entry['ts'], keys, entry['value']])

# with open('telemetry_data.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['timestamp', 'product_id', 'product_name'])  # Write the header

#     for key, values in data.items():
#         for entry in values:
#             timestamp = entry['ts']
#             value_list = entry['value'].strip(',')
#             product_id = value_list[0].strip()
#             product_name = value_list[1].strip() if len(value_list) > 1 else ''
#             writer.writerow([timestamp, product_id, product_name])