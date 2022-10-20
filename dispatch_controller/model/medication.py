from dispatch_controller.config import db, ma
from marshmallow import fields, post_load, validate

class Medication(db.Model):

    __tablename__ = 'medication'

    medid = db.Column(db.Integer, nullable=False, primary_key=True)

    dronid = db.Column(db.Integer, db.ForeignKey("dron.dronid"))

    code = db.Column(db.String(50), nullable=False)

    image = db.Column(db.VARCHAR(200), nullable=False)

    name = db.Column(db.String(50), nullable=False)

    weight = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Medication "{self.medid}">'


class MedicationSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Medication
        sqla_session = db.session

    medid = fields.Integer()
    code = fields.String(validate=validate.Regexp(regex="^[A-Z0-9_]*$", error="Invalid medication code"))
    image = fields.Url(validate=validate.URL(error="Invalid url"))  
    name = fields.String(validate=validate.Regexp(regex="^[A-Za-z0-9_-]*$", error="Invalid medication name"))
    weight = fields.Float()
    dronid = fields.Integer()

    @post_load

    def make_medication(self, data, **kwargs):
        return Medication(**data)