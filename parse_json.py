import json

# Load the JSON data from a file or string
with open('data.json', 'r') as f:
    data = json.load(f)

# Find all obj_id values in the "value" list
obj_ids = []
for item in data['value']:
    if 'obj_id' in item:
        obj_ids.append(item['obj_id'])

# Write the obj_ids to a text file
with open('obj_ids.txt', 'w') as f:
    f.write('$'.join(obj_ids))
