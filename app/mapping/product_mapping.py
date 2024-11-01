from marshmallow import Schema, fields, validate, post_load
from app.models import Order

class ProductMap(Schema):
    id: int = fields.Integer(dump_only=True)
    id_provider: int = fields.Integer(required=True)
    name: str = fields.String(required=True)
    description: str = fields.String(required=True)
    price: float = fields.Float(required=True, validate=validate.Range(min=0))
    stock: int = fields.Integer(required=True, validate=validate.Range(min=0))
    category: str = fields.String(required=True)
    brand: str = fields.String(required=True)
    
    @post_load
    def bind_product(self, data, **kwargs):
        return Order(**data)