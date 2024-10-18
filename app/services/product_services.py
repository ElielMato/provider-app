
from typing import List
from app.models import Product
from app.repositories import ProductRepository
repository = ProductRepository()

class ProductService():

    def save(self, product:Product) -> Product:
        repository.save(product)
        return product
    
    def delete(self, product:Product) -> None:
        repository.delete(product)

    def find(self, id: int) -> 'Product':
        return repository.find(id)

    def find_all(self) -> List['Product']:
        return repository.find_all()
    
    def find_by(self, **kwargs) -> List['Product']:
        return repository.find_by(**kwargs)
    
    def buy(self, product:Product, amount:float) -> Product:
        product.stock += amount
        return repository.save(product)

    def sell(self, product:Product, amount:float) -> Product:
        product.stock -= amount
        return repository.save(product)