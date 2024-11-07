
from typing import List
from app.models import Order
from app.repositories import OrderRepository
order_repository = OrderRepository()

class OrderService():

    def save(self, order:Order) -> Order:
        order_repository.save(order)
        return order
    
    def delete(self, order: Order) -> None:
        order_repository.delete(order)

    def find(self, id: int) -> 'Order':
        return order_repository.find(id)

    def find_all(self) -> List['Order']:
        return order_repository.find_all()
    
    def find_by(self, **kwargs) -> List['Order']:
        return order_repository.find_by(**kwargs)
    
    def find_by_user_id(self, user_id: int) -> List['Order']:
        return order_repository.find_by(id_client=user_id)