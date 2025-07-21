import json
data = {'name': 'Ali','age':25}
json_string = json.dumps(data)  #Convert to json string
print(json_string)

#Convert JSON string back to python dict
parsed_data = json.loads(json_string)
print(parsed_data['name'])