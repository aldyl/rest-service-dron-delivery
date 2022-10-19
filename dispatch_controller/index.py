#!/bin/pyton3
from flask import Flask, jsonify, request

from dispatch_controller.model.dron import Dron, DronSchema

from dispatch_controller.model.medication import Medication, MedicationSchema

from dispatch_controller.model.state_type import StateType
from dispatch_controller.model.model_type import ModelType


app = Flask(__name__)


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
    Medication(0, "MT001", "./image001", "Meoxilina", 23),
    Medication(1, "MT002", "./image002", "CarboMuro", 180),
    Medication(2, "MT003", "./image003", "Miosina", 75),
    Medication(3, "MT004", "./image004", "Chacatre", 130),
    Medication(4, "MT005", "./image005", "Hidrovenote", 45),
    Medication(5, "MT006", "./image006", "Carbafel", 300),
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
