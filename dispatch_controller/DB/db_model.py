
from dispatch_controller.config import db, ma


class Dron(db.Model):

    __tablename__ = 'dron'

    # unique  identifier  for the Dron instance
    dronid = db.Column(db.Integer, primary_key=True)

    batteryload = db.Column(db.Integer)

    dronecargo = db.relationship('Medication', backref='dron')

    model = db.Column(db.String(50), nullable=False)
    serial = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Integer)

class Medication(db.Model):

    __tablename__ = 'medication'
    
    medid = db.Column(db.Integer, nullable=False, primary_key=True)

    dronid = db.Column(db.Integer, db.ForeignKey("dron.dronid"))

    code = db.Column(db.String(50), nullable=False)

    image = db.Column(db.VARCHAR(200), nullable=False)

    name = db.Column(db.String(50), nullable=False)

    weight = db.Column(db.Integer, nullable=False)


class DronSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dron
        sqla_session = db.session

class MedicationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Medication
        sqla_session = db.session
        