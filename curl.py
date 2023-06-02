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

for i in range(1, 101):
    display_name = f"lmaosem{i}"
    ip = f"158.250.17.{i}"
    payload = {
        "display_name": display_name,
        "ip_host_port_tuples": [
            {
                "host": f"{display_name}.ru",
                "ip": ip,
                "port": 80
            }
        ]
    }
    payload_json = json.dumps(payload)
    conn.request("PUT", "/model/webapp/", payload_json, headers)
    res = conn.getresponse()
    data = res.read()
    print(f"Request {i}: {data.decode('utf-8')}")