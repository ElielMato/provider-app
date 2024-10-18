from dataclasses import dataclass
from app import db

@dataclass(init=True, eq=False)
class Product(db.Model):
    """
    Clase que representa un producto de un usuario.
    """
    __tablename__ = "products"
    id: int = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    # id_user: str = db.Column("firstname", db.String(100), nullable=False, unique=True)
    name: str = db.Column("name", db.String(100), nullable=False)
    description: str = db.Column("description", db.String(250), nullable=False)
    stock: str = db.Column("stock", db.Float, nullable=False, default=0)
    price: str = db.Column("price", db.Float, nullable=False, default=0)
    
    def __eq__(self, product: object) -> bool:
        return (self.id == product.id)