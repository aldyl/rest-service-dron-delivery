
import os

from dispatch_controller.config import app, db, db_uri

from dispatch_controller.DB.db_model import Dron as DBdron, Medication as DBmedication

from dispatch_controller.model.dron import Dron
from dispatch_controller.model.medication import Medication

from dispatch_controller.model.state_type import StateType
from dispatch_controller.model.model_type import ModelType

# Data to initialize database with
drones = [

    Dron(0, 50, [], ModelType.LIGTHWEIGHT.value,
         "GH5", StateType.RETURNING.value, 45),
    Dron(1, 90, [], ModelType.HEAVYWEIGHT.value,
         "GH6", StateType.LOADED.value, 365),
    Dron(2, 45, [], ModelType.CRUISERWEIGHT.value,
         "GH7", StateType.DELIVERING.value, 89),
    Dron(3, 10, [], ModelType.CRUISERWEIGHT.value,
         "GH8", StateType.IDLE.value, 287),
    Dron(4, 89, [], ModelType.MIDDLEWEIGHT.value,
         "GH9", StateType.DELIVERED.value, 129),
    Dron(5, 34, [], ModelType.LIGTHWEIGHT.value,
         "GH10", StateType.LOADED.value, 365),
    Dron(6, 90, [], ModelType.LIGTHWEIGHT.value,
         "GH5", StateType.RETURNING.value, 286),
    Dron(7, 100, [], ModelType.HEAVYWEIGHT.value,
         "GH6", StateType.LOADED.value, 346),
    Dron(8, 50, [], ModelType.CRUISERWEIGHT.value,
         "GH7", StateType.DELIVERING.value, 123),
    Dron(9, 46, [], ModelType.CRUISERWEIGHT.value,
         "GH8", StateType.IDLE.value, 80),

]

medications = [
    Medication(0, "MT001", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.hkSYU8xOgNZmWkbzuoV-dQHaE9%26pid%3DApi&f=1&ipt=ea2364891df1b2499f144fbbba99788a5fcce6a527e57109416014adf463d3d5&ipo=images", "Meoxilina", 23, 0),
    Medication(1, "MT002", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.OsXRjEUIIOV6BwGI6ZeGEwHaEL%26pid%3DApi&f=1&ipt=98d4d7fd2b59f3f372d581b129ace3035fa85d80604e57e36639ff3e1bccc9da&ipo=images", "CarboMuro", 180, 5),
    Medication(2, "MT003", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.htSO0GTjaIPU3VUy-jXwiwHaD4%26pid%3DApi&f=1&ipt=ef601d481b9cc5ba2d002b3ca0e59ea7e4ccbc095d8fb798dc543c905c456801&ipo=images", "Miosina", 75, -1),
    Medication(3, "MT004", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.cCQofTvUTwdtzpnWn0msUgHaFo%26pid%3DApi&f=1&ipt=220eefc5328d314e61b567999190cb16c3ace12744c907e27604d2f705baf79e&ipo=images", "Chacatre", 130, -1),
    Medication(4, "MT005", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.OtEK6QBlKgiu4zygAZ1KZAHaFx%26pid%3DApi&f=1&ipt=8b5f508ed13923678934ad2028c23fa48b487e81482359c05456a963c32a394c&ipo=images", "Hidrovenote", 45, 4),
    Medication(5, "MT006", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.55qQqaJ6C4-UL0UxHYlV2QHaDF%26pid%3DApi&f=1&ipt=8ae3c42d91fed0388f71a22fcc4f9a51c19825c50f80cb18f5b4384f03fe672e&ipo=images", "Carbafel", 300, -1),
]


# Delete database file if it exists currently
url = db_uri.replace("sqlite:////","/")
if os.path.exists(url):
     os.remove(url)

# Create the database
db.create_all()

# Iterate over the database

for dron in drones:

     if type(dron) is Dron:
          aux = DBdron(dronid=dron.id, batteryload=dron.battery_load, dronecargo=dron.drone_cargo,
                  model=dron.model, serial=dron.serial, state=dron.state, weight=dron.weight)
          db.session.add(aux)

db.session.commit()

for med in medications:

  
     if type(med) is Medication:
          aux = DBmedication(medid=med.id,  code=med.code, image=med.image,
                       name=med.name, weight=med.weight, dronid=med.dron_id)
          db.session.add(aux)

db.session.commit()


if __name__ == '__main__':
    app.run()
