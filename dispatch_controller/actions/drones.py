"""
This is the drones module and supports all the REST actions for the
drones data
"""

import re
from flask import jsonify, request
from dispatch_controller.config import app, db

from dispatch_controller.model.dron import Dron , DronSchema 

from dispatch_controller.model.medication import Medication,  MedicationSchema

from sqlalchemy import func



def _find_next_id(): 

    result = db.session.query(func.max(Dron.dronid)).first()
    
    return int(result[0])+1

@app.route("/drones", methods=["POST"])
def add_dron():

    if request.is_json:

        result = request.get_json()

        serial = result["serial"]

        exist_dron = ( Dron.query.filter(Dron.serial == serial).one_or_none() )


        if exist_dron is None:

            result["dronid"] = _find_next_id()
            schema = DronSchema()

            new_dron = schema.load(result)

            db.session.add(new_dron)
        
            db.session.commit()
            data = schema.dump(new_dron)
            return data, 201

        else:
            return { "error": "Dron serial exist in database"}, 409

    else:
        return {"error": "Request must be JSON"}, 415






@app.route("/drones", methods=["GET"])
def get_all_drones():
    """
    This function responds to a request for /api/drones
    with the complete lists of drones available
    :return:        json string of list of drones
    """
    # Create the list of drones from our data
    drones = Dron.query.all()
       
    schema = DronSchema(many=True)
    _drones = schema.dump(drones)
    return jsonify(_drones)


@app.route("/drones/<dron_id>", methods=["GET"])
def get_dron(dron_id):
    """
    This function responds to a request for /api/drones/<dron_id>
    
    :return:        json string
    """

    dron = Dron.query.filter(Dron.dronid == dron_id).one_or_none()

    if dron is not None:

        # Serialize the data for the response
        dron_schema = DronSchema()    
        _dron = dron_schema.dump(dron)
        
        return jsonify(_dron), 200

    # Otherwise, nope, didn't find that id
    else:
        return  { "error" : "not found for Id: {dron_id}".format(dron_id=dron_id)} , 404

@app.route("/drones/<dron_id>/cargo", methods=["GET"])
def get_dron_cargo(dron_id):
    """
    This function responds to a request for /api/drones/<dron_id>/cargo
    
    :return:        json string
    """

    dron = Dron.query.filter(Dron.dronid == dron_id).one_or_none()

    if dron is not None:

        # Serialize the data for the response
        dron_schema = MedicationSchema(many=True)    
        _dron = dron_schema.dump(dron.dronecargo)
        
        return jsonify(_dron), 200

    # Otherwise, nope, didn't find that id
    else:
        return  { "error" : "not found for Id: {dron_id}".format(dron_id=dron_id)} , 404


@app.route("/drones/<dron_id>/battery", methods=["GET"])
def get_dron_battery(dron_id):
    """
    This function responds to a request for /api/drones/<dron_id>/battery
    To check if the battery is is good.
    :return:        json string
    """

    dron = Dron.query.filter(Dron.dronid == dron_id).one_or_none()

    if dron is not None:

        # Serialize the data for the response
        dron_schema = DronSchema()    
        _dron = dron_schema.dump(dron)
        
        batteryload = _dron.get("batteryload" )

        return { "dronid" : dron_id, "batteryload" : batteryload}, 200

    # Otherwise, nope, didn't find that id
    else:
        return  { "error" : "not found for Id: {dron_id}".format(dron_id=dron_id)} , 404

@app.route("/drones/readyforload", methods=["GET"])
def get_dron_ready_for_load():
    """
    This function responds to a request for /api/drones/readyforload
    To check drones ready for load cargo
    :return:        json string
    """

    dron = Dron.query.filter(Dron.batteryload > 25).filter(Dron.state == "IDLE").all()

    if dron is not None:

        # Serialize the data for the response
        dron_schema = DronSchema(many=True)    
        _dron = dron_schema.dump(dron)
        
        return jsonify(_dron), 200

    # Otherwise, nope, didn't find that id
    else:
        return  { "error" : "Not available"} , 404

