#!/bin/pyton3

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index(): return "Hello"


drones = [
    {'serial': '930#sd', "model": "Ligthweigth",
     "weight": 450,
     "batery_capacity": "90",
     "state": "IDLE",
     "carry": {}
     },
]

medications = [
    {"name": "Sust-01_q",
     "weight": "300",
     "code": "sasas212_121",
     "image": "./image0.jpg"
     }
]


@app.route("/drones")
def get_all_drones():
    return jsonify(drones)


@app.route("/drones/create", methods=["POST"])
def create_drones():
    drones.append(request.get_json())
    return "", 204

@app.route("/medications")
def get_all_medications():
    return jsonify(medications)


@app.route("/medications/create", methods=["POST"])
def create_medication():
    medications.append(request.get_json())
    return "", 204

