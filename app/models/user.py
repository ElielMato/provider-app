from dataclasses import dataclass
from app import db

@dataclass(init=True, eq=False)
class User(db.Model):
    """
    Clase que representa un usuario del sistema con distintos perfiles.
    """
    __tablename__ = "users"
    id: int = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    firstname: str = db.Column("firstname", db.String(100), nullable=False)
    lastname: str = db.Column("lastname", db.String(100), nullable=False)
    email: str = db.Column("email", db.String(250), unique=True, nullable=False)
    password: str = db.Column("password", db.String(254), nullable=False)
    phone: str = db.Column("phone", db.String(100), unique=True, nullable=False)
    address: str = db.Column("address", db.String(250), nullable=False)
    country: str = db.Column("country", db.String(100), nullable=False)
    state: str = db.Column("state", db.String(100), nullable=False)
    zip_code: str = db.Column("zip_code", db.String(100), nullable=False)
    
    def __eq__(self, user: object) -> bool:
        return (self.id == user.id and self.email == user.email and
                self.firstname == user.firstname and self.lastname == user.lastname and
                self.phone == user.phone)