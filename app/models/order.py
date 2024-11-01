from dataclasses import dataclass
from datetime import datetime
from app import db

@dataclass(init=True, eq=False)
class Order(db.Model):
    """
    Clase que representa una orden de compra de un usuario.
    """
    __tablename__ = 'orders'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_client: int = db.Column(db.Integer, nullable=False)
    products: list = db.Column(db.JSON, nullable=False)
    total: int = db.Column(db.Float, nullable=False)
    order_date: datetime = db.Column(db.Date, default=datetime.utcnow, nullable=False)

    def __eq__(self, order: object) -> bool:
        return (self.id == order.id)
