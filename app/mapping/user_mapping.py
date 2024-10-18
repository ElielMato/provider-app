from marshmallow import Schema, fields, validate, post_load
from app.models import User

class UserMap(Schema):

    id:int = fields.Integer(dump_only=True)
    firstname:str = fields.String(required=True)
    lastname:str = fields.String(required=True)
    email:str = fields.String(required=True, validate=validate.Email())
    phone:str = fields.String(required=True)
    address:str = fields.String(required=True)
    state:str = fields.String(required=True)
    country:str = fields.String(required=True)
    zip_code:str = fields.String(required=True)
    password:str = fields.String(load_only=True, required=True)
    
    @post_load
    def bind_user(self, data, **kwargs):
        return User(**data)