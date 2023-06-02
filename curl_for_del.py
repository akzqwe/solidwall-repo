
import http.client
import json
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE

# Set variables for the IP address and csrf token
ip_address = "X"
csrf_token = "X"

conn = http.client.HTTPSConnection(ip_address, 8443, context=context)
headers = {
  '-csrf-token': csrf_token,
  'X-Requested-With': 'XMLHttpRequest',
  'Content-Type': 'application/json',
  'Cookie': 'sw_session=X'
}

# Load the JSON data from a file or string
with open('data.json', 'r') as f:
    data = json.load(f)

# Iterate over the "value" list and send DELETE requests for each obj_id
for item in data['value']:
    if 'obj_id' in item:
        obj_id = item['obj_id']
        path = f"/model/webapp/{obj_id}/"
        conn.request("DELETE", path, headers=headers)
        res = conn.getresponse()
        data = res.read()
        print(f"DELETE {path}: {data.decode('utf-8')}")