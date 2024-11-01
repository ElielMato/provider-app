
from typing import List
from app.models import Product
from app.repositories import ProductRepository
product_repository = ProductRepository()

class ProductService():

    def save(self, product:Product) -> Product:
        product_repository.save(product)
        return product
    
    def delete(self, product:Product) -> None:
        product_repository.delete(product)

    def find(self, id: int) -> 'Product':
        return product_repository.find(id)

    def find_all(self) -> List['Product']:
        return product_repository.find_all()
    
    def find_by(self, **kwargs) -> List['Product']:
        return product_repository.find_by(**kwargs)
    
    def find_by_user_id(self, user_id: int):
        return product_repository.find_by_user_id(user_id)
    
    def buy(self, product:Product, amount:float) -> Product:
        product.stock += amount
        return product_repository.save(product)

    def sell(self, product:Product, amount:float) -> Product:
        product.stock -= amount
        return product_repository.save(product)