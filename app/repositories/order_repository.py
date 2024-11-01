from typing import List
from app.models import Order
from app import db
from app.repositories import CreateAbstractRepository, ReadAbstractRepository, DeleteAbstractRepository

class OrderRepository(CreateAbstractRepository, ReadAbstractRepository, DeleteAbstractRepository):

    def save(self, order:Order) -> Order:
        db.session.add(order)
        db.session.commit()
        return order
    
    def delete(self, order:Order) -> None:
        db.session.delete(order)
        db.session.commit()
    
    def find(self, id: int) -> 'Order':
        return Order.query.get(id)

    def find_all(self, ) -> List['Order']:
        return Order.query.all()
    
    def find_by(self, **kwargs) -> List['Order']:
        return Order.query.filter_by(**kwargs).all()
    
    def find_by_user_id(self, user_id: int):
        return Order.query.filter_by(id_provider=user_id).all()