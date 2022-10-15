import requests
import random
import string
import secrets

API_SERVER = "http://localhost:5000"

test = [

    {

        "type": "POST",
        "endpoint": "/drones",
        "data": {"serial": "930#sd",
                 "model": "Ligthweigth",
                 "weight": 450,
                 "battery_capacity": "90",
                 "state": "IDLE",
                 "carry": ["as", "sd"]},

    },

    {
        "type": "GET",
        "endpoint": "/drones",
    },


    {

        "type": "POST",
        "endpoint": "/medications",
        "data": {"code": "".join(secrets.choice(string.ascii_letters + string.digits) for x in range(6)),
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

    elif r["type"] == "GET":
        response = requests.get(API_SERVER + r["endpoint"])

    else:
        continue

    print(r["type"], r["endpoint"], response.status_code)
