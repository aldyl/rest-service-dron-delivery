import requests
import random
import string
import secrets

from model.state_type import StateType
from model.model_type import ModelType

API_SERVER = "http://localhost:5000"

test = [

    {
        "type": "POST",
        "endpoint": "/drones",
        "data": {"serial": "".join(secrets.choice(string.ascii_letters + string.digits) for x in range(100)),
                 "model": ModelType.RANDOM.value,
                 "weight": int(random.random()*1000/2),
                 "batteryload": int(random.random()*100),
                 "state": StateType.RANDOM.value, }

    },

    {
        "type": "GET",
        "endpoint": "/drones",
    },


    {

        "type": "POST",
        "endpoint": "/medications",
        "data": {
                 "code": "".join(secrets.choice(string.ascii_uppercase + string.digits+"_") for x in range(10)),
                 "image": "http://www.cu",
                 "name": "".join(secrets.choice(string.ascii_letters + string.digits+"_-") for x in range(10)),
                 "weight": int(random.random()*1000/2),
                 "dronid": int(random.random()*10),
                 },

    },

    {
        "type": "GET",
        "endpoint": "/medications",
    },

]

for r in test:
    if r["type"] == "POST":
        response = requests.post(API_SERVER + r["endpoint"], json=r["data"])
        print(r["type"], r["endpoint"], response.status_code, response.text)

    elif r["type"] == "GET":
        response = requests.get(API_SERVER + r["endpoint"])
        print(r["type"], r["endpoint"], response.status_code)

    else:
        continue
