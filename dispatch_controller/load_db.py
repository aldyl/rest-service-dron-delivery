
import os

from dispatch_controller.config import app, db, db_uri

from dispatch_controller.model.dron import Dron
from dispatch_controller.model.medication import Medication
from dispatch_controller.model.model_type import ModelType
from dispatch_controller.model.state_type import StateType


# Data to initialize database with
drones = [

    {"dronid": 0,  "batteryload":   50,  "model": ModelType.LIGTHWEIGHT.value,
        "serial":    "GH5", "state":  StateType.RETURNING.value, "weight": 50},
    {"dronid": 1,  "batteryload":   90,  "model": ModelType.HEAVYWEIGHT.value,
        "serial":    "GH6",   "state":     StateType.LOADED.value, "weight": 460},
    {"dronid": 2,  "batteryload":   45,  "model": ModelType.CRUISERWEIGHT.value,
        "serial":    "GH7",   "state":     StateType.DELIVERING.value, "weight": 420},
    {"dronid": 3,  "batteryload":   10,  "model": ModelType.CRUISERWEIGHT.value,
        "serial":    "GH8",   "state":     StateType.IDLE.value, "weight": 60},
    {"dronid": 4,  "batteryload":   89,  "model": ModelType.MIDDLEWEIGHT.value,
        "serial":    "GH9",   "state":     StateType.DELIVERED.value, "weight": 50},
    {"dronid": 5,  "batteryload":   34,  "model": ModelType.LIGTHWEIGHT.value,
        "serial":    "GH10",  "state":     StateType.LOADED.value, "weight": 400},
    {"dronid": 6,  "batteryload":   90,  "model": ModelType.LIGTHWEIGHT.value,
        "serial":    "GH523", "state":      StateType.RETURNING.value, "weight": 40},
    {"dronid": 7,  "batteryload":   100, "model": ModelType.HEAVYWEIGHT.value,
        "serial":    "GH62",  "state":     StateType.LOADED.value, "weight": 360},
    {"dronid": 8,  "batteryload":   50,  "model": ModelType.CRUISERWEIGHT.value,
        "serial":    "GH73",  "state":     StateType.DELIVERING.value, "weight": 250},
    {"dronid": 9,  "batteryload":   46,  "model": ModelType.CRUISERWEIGHT.value,
        "serial":    "GH84",  "state":     StateType.IDLE.value, "weight": 80},

]

medications = [
    {"medid": 0, "code": "MT001", "image":  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.hkSYU8xOgNZmWkbzuoV-dQHaE9%26pid%3DApi&f=1&ipt=ea2364891df1b2499f144fbbba99788a5fcce6a527e57109416014adf463d3d5&ipo=images",  "name": "Meoxilina", "weight": 23, "dronid":  1},
    {"medid": 1, "code": "MT002", "image":  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.OsXRjEUIIOV6BwGI6ZeGEwHaEL%26pid%3DApi&f=1&ipt=98d4d7fd2b59f3f372d581b129ace3035fa85d80604e57e36639ff3e1bccc9da&ipo=images",  "name": "CarboMuro", "weight": 180, "dronid":  1},
    {"medid": 2, "code": "MT003", "image":  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.htSO0GTjaIPU3VUy-jXwiwHaD4%26pid%3DApi&f=1&ipt=ef601d481b9cc5ba2d002b3ca0e59ea7e4ccbc095d8fb798dc543c905c456801&ipo=images",  "name": "Miosina", "weight": 75, "dronid":  1},
    {"medid": 3, "code": "MT004", "image":  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.cCQofTvUTwdtzpnWn0msUgHaFo%26pid%3DApi&f=1&ipt=220eefc5328d314e61b567999190cb16c3ace12744c907e27604d2f705baf79e&ipo=images",  "name": "Chacatre", "weight": 130, "dronid":  -1},
    {"medid": 4, "code": "MT005", "image":  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.OtEK6QBlKgiu4zygAZ1KZAHaFx%26pid%3DApi&f=1&ipt=8b5f508ed13923678934ad2028c23fa48b487e81482359c05456a963c32a394c&ipo=images",  "name": "Hidrovenote", "weight": 45, "dronid":  -1},
    {"medid": 5, "code": "MT006", "image":  "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.55qQqaJ6C4-UL0UxHYlV2QHaDF%26pid%3DApi&f=1&ipt=8ae3c42d91fed0388f71a22fcc4f9a51c19825c50f80cb18f5b4384f03fe672e&ipo=images",  "name": "Carbafel", "weight": 300, "dronid": -1},
]


# Delete database file if it exists currently
url = db_uri.replace("sqlite:////", "/")
if os.path.exists(url):
    os.remove(url)

# Create the database
db.create_all()

# Iterate over the database

for dron in drones:
    aux = Dron(dronid=dron.get("dronid"), batteryload=dron.get("batteryload"), model=dron.get(
        "model"), serial=dron.get("serial"), state=dron.get("state"), weight=dron.get("weight"))
    db.session.add(aux)

db.session.commit()

for med in medications:
    aux = Medication(medid=med.get("medid"),  code=med.get("code"), image=med.get("image"),
                     name=med.get("name"), weight=med.get("weight"), dronid=med.get("dronid"))
    db.session.add(aux)

db.session.commit()


if __name__ == '__main__':
    app.run()
