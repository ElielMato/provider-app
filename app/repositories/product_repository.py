from typing import List
from app.models import Product
from app import db
from app.repositories import CreateAbstractRepository, ReadAbstractRepository, DeleteAbstractRepository

class ProductRepository(CreateAbstractRepository, ReadAbstractRepository, DeleteAbstractRepository):

    def save(self, product:Product) -> Product:
        db.session.add(product)
        db.session.commit()
        return product
    
    def delete(self, product:Product) -> None:
        db.session.delete(product)
        db.session.commit()
    
    def find(self, id: int) -> 'Product':
        return Product.query.get(id)

    def find_all(self, ) -> List['Product']:
        return Product.query.all()
    
    def find_by(self, **kwargs) -> List['Product']:
        return Product.query.filter_by(**kwargs).all()