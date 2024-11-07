import logging
from flask import Blueprint, request
from app.mapping import ProductMap
from app.services import ProductService, UserServices
from app.mapping import MessageMap
from app.services import MessageBuilder

product_bp = Blueprint('product', __name__)
product_map = ProductMap()
product_service = ProductService()
user_service = UserServices()

@product_bp.route('/products/<int:id>', methods=['GET'])
def get(id: int):
    product = product_service.find(id)
    if product:
        message_map, message_finish = message_create(product_map.dump(product, many=False), 'Se encontró el producto')
        return message_map.dump(message_finish), 200
    else:
        message_map, message_finish = message_create(None, f'No se encontró el producto con ID {id}')
        return message_map.dump(message_finish), 404

@product_bp.route('/products/user/<int:id>', methods=['GET'])
def get_by_user_id(id: int):
    user = user_service.find(id)
    if not user:
        message_map, message_finish = message_create([], f'No se encontró el usuario con ID {id}')
        return message_map.dump(message_finish), 404

    products = product_service.find_by_user_id(id)
    
    if products:
        message_map, message_finish = message_create(
            {'products': product_map.dump(products, many=True)}, 
            f'Se encontraron los productos del usuario con ID {id}'
        )
        return message_map.dump(message_finish), 200
    else:
        message_map, message_finish = message_create(
            {'products': []}, 
            f'No se encontraron productos para el usuario con ID {id}'
        )
        return message_map.dump(message_finish), 200

@product_bp.route('/products', methods=['GET'])
def get_all():
    products = product_service.find_all()
    message_map, message_finish = message_create({'products': product_map.dump(products, many=True)}, 'Se encontro todos los productos')
    return message_map.dump(message_finish), 200

@product_bp.route('/products', methods=['POST'])
def post():
    product = product_map.load(request.json)
    user = user_service.find(product.id_provider)

    if not user:
        message_map, message_finish = message_create([], f'No existe un usuaro con la ID {product.id_provider}')
        return message_map.dump(message_finish), 404
    
    product_service.save(product)
    message_map, message_finish = message_create(product_map.dump(product), 'Producto Creado')
    return message_map.dump(message_finish), 201

@product_bp.route('/products/<int:id>', methods=['PUT'])
def update(id: int):
    product = product_service.find(id)
    if not product:
        message_map, message_finish = message_create({}, f'Producto con ID {id} no encontrado')
        return message_map.dump(message_finish), 404

    updated_data = request.json
    
    for key, value in updated_data.items():
        setattr(product, key, value)
    
    updated_product = product_service.save(product)
    
    message_map, message_finish = message_create(product_map.dump(updated_product), f'Producto con ID {id} Actualizado')
    return message_map.dump(message_finish), 200

@product_bp.route('/products/<int:id>', methods=['DELETE'])
def delete(id: int):
    product = product_service.find(id)
    if product:
        product_service.delete(product)
        message_map, message_finish = message_create([], f'Producto con ID {id} Eliminado')
        return message_map.dump(message_finish), 200
    else:
        message_map, message_finish = message_create([], f'Producto con ID {id} no encontrado')
        return message_map.dump(message_finish), 404

@product_bp.route('/products/<int:id>/add-stock', methods=['PUT'])
def add_stock(id: int):
    product = product_service.find(id)
    if not product:
        message_map, message_finish = message_create({}, f'Producto con ID {id} no encontrado')
        return message_map.dump(message_finish), 404

    stock_to_add = request.json.get('stock_to_add')
    
    if not isinstance(stock_to_add, int) or stock_to_add <= 0:
        message_map, message_finish = message_create({}, 'La cantidad de stock a agregar debe ser un número entero positivo')
        return message_map.dump(message_finish), 400

    product.stock += stock_to_add
    updated_product = product_service.save(product)
    
    message_map, message_finish = message_create(
        product_map.dump(updated_product), 
        f'Stock actualizado para el producto con ID {id}. Nuevo stock: {updated_product.stock}'
    )
    return message_map.dump(message_finish), 200

def message_create(data, message):
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message(message).add_data(data).build()
    return message_map,message_finish