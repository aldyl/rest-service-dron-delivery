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
    Dron(50, [], ModelType.LIGTHWEIGHT.value,
         "GH5", StateType.RETURNING.value, 100),
    Dron(90, [], ModelType.HEAVYWEIGHT.value,
         "GH6", StateType.LOADED.value, 445),
    Dron(90, [], ModelType.CRUISERWEIGHT.value,
         "GH7", StateType.DELIVERING.value, 445),
    Dron(80, [], ModelType.CRUISERWEIGHT.value,
         "GH8", StateType.IDLE.value, 90),
    Dron(10, [], ModelType.MIDDLEWEIGHT.value,
         "GH9", StateType.DELIVERED.value, 100),
    Dron(30, [], ModelType.LIGTHWEIGHT.value,
         "GH10", StateType.LOADED.value, 445),
]

medications = [
    Medication("MT001", "./image001", "Meoxilina", 23),
    Medication("MT002", "./image002", "CarboMuro", 180),
    Medication("MT003", "./image003", "Miosina", 75),
    Medication("MT004", "./image004", "Chacatre", 130),
    Medication("MT005", "./image005", "Hidrovenote", 45),
    Medication("MT006", "./image006", "Carbafel", 300),
]

################################
# Drones


@app.route("/drones", methods=["POST"])
def add_dron():

    dron = DronSchema().load(request.get_json())
    drones.append(dron)
    return "Dron added", 204


@app.route("/drones", methods=["GET"])
def get_all_drones():

    schema = DronSchema(many=True)
    _drones = schema.dump(drones)
    return jsonify(_drones)


@app.route("/drones/<serial>", methods=["GET"])
def get_dron(serial):

    schema = DronSchema(many=True)
    dron = schema.dump(filter(lambda x: x.serial == serial, drones))
    return jsonify(dron)

################################
# Medication


@app.route("/medications", methods=["POST"])
def add_medication():

    med = MedicationSchema().load(request.get_json())
    medications.append(med)
    return "Good", 201


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
