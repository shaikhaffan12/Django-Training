import requests
import json

URL = "http://127.0.0.1:8000/stuinsert/"

data = {
    'name' : 'rohit',
    'roll' : 50,
    'city' : 'pune'
}

json_data = json.dumps(data)

r = requests.post(url= URL, data= json_data)

data1 = r.json()
print(data1)