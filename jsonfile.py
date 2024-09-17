import json
data ={
"Name" :["shipra","vidhi","nikita"],
"Age" :[20,22,19],
"City":["ghaziabad","delhi","noida"]

}
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Read data from the JSON file
with open('data.json', 'r') as file:
    loaded_data = json.load(file)

print(loaded_data)