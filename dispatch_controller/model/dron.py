
from marshmallow import Schema, fields, post_load

class Dron(object):

    def __init__(self, battery_capacity, carry, model, serial, state, weight):
        self.battery_capacity = battery_capacity
        self.carry = carry
        self.model = model
        self.serial = serial
        self.state = state
        self.weight = weight

    def __repr__(self) -> str:
        return 'Dron(model=%s, serial=%s, state=%s, battery_capacity=%s)' % (self.model, self.serial, self.state, self.battery_capacity)

class DronSchema(Schema):

    battery_capacity = fields.Integer()
    carry = fields.List(fields.String())
    model = fields.String()
    serial = fields.String()
    state = fields.String()
    weight = fields.Float()

    @post_load

    def make_dron(self, data, **kwargs):

        return Dron(**data)

