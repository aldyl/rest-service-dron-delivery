
from marshmallow import Schema, fields, post_load

class Dron(object):

    def __init__(self, id:int, battery_load:int, drone_cargo:list, model:str, serial:str, state:str, weight:int):
        self.id = id
        self.battery_load = battery_load
        self.drone_cargo = drone_cargo
        self.model = model
        self.serial = serial
        self.state = state
        self.weight = weight

    def __repr__(self) -> str:
        return 'Dron(model=%s, serial=%s, state=%s, battery_capacity=%s)' % (self.model, self.serial, self.state, self.battery_capacity)

    def get_id(self):
        return self.id

class DronSchema(Schema):


    id = fields.Integer()
    battery_load = fields.Integer()
    drone_cargo = fields.List(fields.String())
    model = fields.String()
    serial = fields.String()
    state = fields.String()
    weight = fields.Float()

    @post_load

    def make_dron(self, data, **kwargs):

        return Dron(**data)

