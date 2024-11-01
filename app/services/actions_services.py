from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Product():
    name: str
    price: float
    category: str
    license: str
    stock: float

class Command(ABC):
    @abstractmethod
    def execute(self, product: Product):
        pass

class VerificationStock(Command):
    def execute(self, product: Product):
        if product.stock > 0:
            print(f"Producto '{product.name}' tiene stock: {product.stock} artículos disponibles.")
        else:
            print(f"Producto '{product.name}' está agotado.")

class SendMail(Command):
    def execute(self, producto: Product):
        print(f"Correo enviado al dueño del producto '{producto.name}'.")

class ModificationStock(Command):
    def execute(self, producto: Product):
        producto.stock += 1
        print(f"El stock del producto '{producto.name}' ha sido actualizado. Nuevo stock: {producto.stock}")

class ActivateKey(Command):
    def execute(self, producto: Product):
        print(f"La key de licencia '{producto.license}' para el producto '{producto.name}' ha sido activada.")

class PayProduct(Command):
    def execute(self, producto: Product):
        print(f"El pago del producto '{producto.name}' ha sido procesado.")

class DesativateKey(Command):
    def execute(self, producto: Product):
        print(f"La key de licencia '{producto.license}' para el producto '{producto.name}' ha sido desactivada.")

@dataclass
class Action():
    
    def __init__(self):
        self.actions = []
    
    def add(self, action: Command):
        self.actions.append(action)

    def remove(self, id_action: Command):
        del(self.actions[id_action])

    def execute(self, product: Product):
        for action in self.actions:
            action.execute(product)

if __name__ == '__main__':
    product = Product('Caramelos', 100, 'Golosinas', '#HADDSD8F4D4FS1VSD4SS', 10)

    action = Action()
    action.add(VerificationStock())
    action.add(SendMail())
    action.add(ModificationStock())
    action.add(ActivateKey())
    action.add(PayProduct())
    action.add(DesativateKey())
    action.remove(2)
    action.execute(product)