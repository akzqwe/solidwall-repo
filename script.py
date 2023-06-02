import json

records = []

for i in range(1, 101):
    display_name = f"secsem{i}"
    ip = f"158.250.17.{i}"
    record = {
        "display_name": display_name,
        "ip_host_port_tuples": [
            {
                "host": display_name + ".ru",
                "ip": ip,
                "port": 80
            }
        ]
    }
    records.append(record)

with open("records.json", "w") as f:
    json.dump(records, f, indent=4)