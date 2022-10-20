from flask import jsonify, request
from dispatch_controller.config import app, db

from dispatch_controller.model.medication import Medication,  MedicationSchema

from sqlalchemy import func

def _find_next_id(): 

    result = db.session.query(func.max(Medication.medid)).first()
    
    return int(result[0])+1

@app.route("/medications", methods=["POST"])
def add_medication():

    if request.is_json:
        
        result = request.get_json()
    
        result['medid'] = _find_next_id()

        schema = MedicationSchema()

        new_med = schema.load(result)

        db.session.add(new_med)
        db.session.commit()

        data = schema.dump(new_med)
        return data, 201

    else:
        return {"error": "Request must be JSON"}, 415


@app.route("/medications", methods=["GET"])
def get_all_medication():
    """
    This function responds to a request for /api/medications
    with the complete lists of medication available
    :return:        json string of list of medication
    """
    # Create the list of drones from our data
    med = Medication.query.order_by(Medication.medid).all()
       
    schema = MedicationSchema(many=True)
    _med = schema.dump(med)
    return jsonify(_med)


@app.route("/medications/<medication_id>", methods=["GET"])
def get_medication_code(medication_id):
    """
    This function responds to a request for /api/medications/<medication_id>
    with the medication 
    :return:        json
    """
    med = Medication.query.filter(Medication.medid == medication_id).one_or_none()


    if med is not None:

        # Serialize the data for the response
        med_schema = MedicationSchema()    
    
        _med = med_schema.dump(med)
        return jsonify(_med)

    # Otherwise, nope, didn't find that person
    else:
        return  { "error" : "not found for Id: {medication_id}".format(medication_id=medication_id)} , 404


