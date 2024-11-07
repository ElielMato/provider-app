from marshmallow import Schema, fields, post_load
from app.models import Order

class OrderMap(Schema):
    id = fields.Int(dump_only=True)
    id_client = fields.Int(required=True)
    products = fields.List(fields.Dict(), required=True)
    total = fields.Float(required=True)
    order_date = fields.DateTime(dump_only=True)

    @post_load
    def bind_user(self, data, **kwargs):
        return Order(**data)