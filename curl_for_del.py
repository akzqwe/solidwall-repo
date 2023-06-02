
import http.client
import json
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_NONE

# Set variables for the IP address and csrf token
ip_address = "10.2.145.50"
csrf_token = "OTFmMzA4MzAtN2RlZC00NWY1LWFmYTktZGY1MDExYmU3ZDA1"

conn = http.client.HTTPSConnection(ip_address, 8443, context=context)
headers = {
  '-csrf-token': csrf_token,
  'X-Requested-With': 'XMLHttpRequest',
  'Content-Type': 'application/json',
  'Cookie': 'sw_session=616ebb29-a41a-4dae-bf2c-3409b887e99f.hro8gXuKf4mz62drkLUNQodt2Wo15ZMyunCTW35Ys50'
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