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

# Set the obj_id for the DELETE request
obj_id = "X"
path = f"/model/webapp/{obj_id}/"

# Send the DELETE request and print the response data
conn.request("DELETE", path, headers=headers)
res = conn.getresponse()
data = res.read()
print(f"DELETE {path}: {data.decode('utf-8')}")