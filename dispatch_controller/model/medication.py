from marshmallow import Schema, fields, post_load

class Medication(object):
    def __init__(self, id, code, image, name, weight ):
        
        self.id = id
        self.code = code
        self.image = image
        self.name = name
        self.weight = weight
        
    def __repr__(self) -> str:
        return '<Medication(name=%s, code: %s)' % (self.name, self.code)
    
    def get_id(self):
        return self.id    

class MedicationSchema(Schema):

    id = fields.Integer()
    code = fields.String()
    image = fields.Url()
    name = fields.String()
    weight = fields.Float()

    @post_load

    def make_medication(self, data, **kwargs):

        return Medication(**data)