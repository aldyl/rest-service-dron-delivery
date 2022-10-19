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
        "data": {"serial": "".join(secrets.choice(string.ascii_letters + string.digits) for x in range(6)),
                 "model": ModelType.RANDOM.value,
                 "weight": int(random.random()*1000/2),
                 "battery_capacity": int(random.random()*100),
                 "state": StateType.RANDOM.value,
                 "carry": []},

    },

    {
        "type": "GET",
        "endpoint": "/drones",
    },

    
    {

        "type": "POST",
        "endpoint": "/medications",
        "data": {"id":"10",
                 "code": "".join(secrets.choice(string.ascii_letters + string.digits) for x in range(6)),
                 "image": "http://www.cu",
                 "name": "".join(secrets.choice(string.ascii_letters + string.digits) for x in range(6)),
                 "weight": int(random.random()*1000/2)},

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

    
