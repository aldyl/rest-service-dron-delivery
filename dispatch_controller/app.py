#!/bin/pyton3
from flask import jsonify, request

from dispatch_controller.model.dron import Dron, DronSchema

from dispatch_controller.model.medication import Medication, MedicationSchema

from dispatch_controller.model.state_type import StateType
from dispatch_controller.model.model_type import ModelType

from dispatch_controller.config import app, db


@app.route("/")
def index(): return "Welcome to Drones Dispath Controller"

drones = [
    Dron(0, 50, [], ModelType.LIGTHWEIGHT.value,
         "GH5", StateType.RETURNING.value, 100),
    Dron(1, 90, [], ModelType.HEAVYWEIGHT.value,
         "GH6", StateType.LOADED.value, 445),
    Dron(2, 90, [], ModelType.CRUISERWEIGHT.value,
         "GH7", StateType.DELIVERING.value, 445),
    Dron(3, 80, [], ModelType.CRUISERWEIGHT.value,
         "GH8", StateType.IDLE.value, 90),
    Dron(4, 10, [], ModelType.MIDDLEWEIGHT.value,
         "GH9", StateType.DELIVERED.value, 100),
    Dron(5, 30, [], ModelType.LIGTHWEIGHT.value,
         "GH10", StateType.LOADED.value, 445),
]

medications = [
    Medication(0, "MT001", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.hkSYU8xOgNZmWkbzuoV-dQHaE9%26pid%3DApi&f=1&ipt=ea2364891df1b2499f144fbbba99788a5fcce6a527e57109416014adf463d3d5&ipo=images", "Meoxilina", 23, 3),
    Medication(1, "MT002", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.OsXRjEUIIOV6BwGI6ZeGEwHaEL%26pid%3DApi&f=1&ipt=98d4d7fd2b59f3f372d581b129ace3035fa85d80604e57e36639ff3e1bccc9da&ipo=images", "CarboMuro", 180, 5),
    Medication(2, "MT003", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.htSO0GTjaIPU3VUy-jXwiwHaD4%26pid%3DApi&f=1&ipt=ef601d481b9cc5ba2d002b3ca0e59ea7e4ccbc095d8fb798dc543c905c456801&ipo=images", "Miosina", 75, -1),
    Medication(3, "MT004", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.cCQofTvUTwdtzpnWn0msUgHaFo%26pid%3DApi&f=1&ipt=220eefc5328d314e61b567999190cb16c3ace12744c907e27604d2f705baf79e&ipo=images", "Chacatre", 130, -1),
    Medication(4, "MT005", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.OtEK6QBlKgiu4zygAZ1KZAHaFx%26pid%3DApi&f=1&ipt=8b5f508ed13923678934ad2028c23fa48b487e81482359c05456a963c32a394c&ipo=images", "Hidrovenote", 45, 4),
    Medication(5, "MT006", "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.55qQqaJ6C4-UL0UxHYlV2QHaDF%26pid%3DApi&f=1&ipt=8ae3c42d91fed0388f71a22fcc4f9a51c19825c50f80cb18f5b4384f03fe672e&ipo=images", "Carbafel", 300, -1),
]

def _find_next_id(collection): return max(c.get_id() for c in collection) + 1

################################
# Drones

@app.route("/drones", methods=["POST"])
def add_dron():

    if request.is_json:

        result = request.get_json()

        result["id"] = _find_next_id(drones)

        dron = DronSchema().load(result)

        drones.append(dron)

        return result, 201

    else:
        return {"error": "Request must be JSON"}, 415


@app.route("/drones", methods=["GET"])
def get_all_drones():

    schema = DronSchema(many=True)
    _drones = schema.dump(drones)
    return jsonify(_drones)


@app.route("/drones/<id>", methods=["GET"])
def get_dron(id):

    schema = DronSchema(many=True)
    dron = schema.dump(filter(lambda x: x.id == int(id), drones))
    return jsonify(dron)

################################
# Medication


@app.route("/medications", methods=["POST"])
def add_medication():

    result = request.get_json()
    med = MedicationSchema().load(result)
    medications.append(med)
    return get_medication_code(result["code"]), 201


@app.route("/medications", methods=["GET"])
def get_all_medication():

    schema = MedicationSchema(many=True)
    _med = schema.dump(medications)
    return jsonify(_med)


@app.route("/medications/<code>", methods=["GET"])
def get_medication_code(code):

    schema = MedicationSchema(many=True)
    _med = schema.dump(filter(lambda x: x.code == code, medications))
    return jsonify(_med)


if __name__ == '__main__':
    app.run()
