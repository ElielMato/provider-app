from dataclasses import dataclass
from app import db

@dataclass(init=True,eq=False)
class User(db.Model):
    """
    Clase que representa un usuario del sistema con distintos perfiles.
    """
    __tablename__ = "users"
    id:int = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    firstname:str = db.Column("nombre", db.String(100), nullable=False)
    lastname:str = db.Column("apellido", db.String(100), nullable=False)
    email:str = db.Column("email", db.String(250), unique=True, nullable=False)
    password:str = db.Column("contrasena", db.String(100), nullable=False)
    phone:str = db.Column("telefono", db.String(100), unique=True, nullable=False)
    address:str = db.Column("direccion", db.String(250), nullable=False)
    country:str = db.Column("pais", db.String(100), nullable=False)
    province:str = db.Column("provincia", db.String(100), nullable=False)
    zip_code:str = db.Column("codigo_postal", db.String(100), nullable=False)
    
    def __eq__(self, user: object) -> bool:
        return self.email == user.email and self.firstname == user.firstname and self.lastname == user.lastname
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self