
from dispatch_controller.config import db, ma
from marshmallow import fields, post_load, validate

from dispatch_controller.model.model_type import ModelType


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

    def __repr__(self):
        return f'<Dron "{self.dronid}">'


class DronSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Dron
        sqla_session = db.session

    dronid = fields.Integer(required=True)
    batteryload = fields.Integer(validate=validate.Range(min_inclusive=0, max_inclusive=100, error='Value in percent'))
    model = fields.String()
    serial = fields.String(validate=validate.Length(min=1, max=100, error='100 characters max'))
    state = fields.String()
    weight = fields.Float()

    @post_load
    def make_dron(self, data, **kwargs):

        return Dron(**data)
