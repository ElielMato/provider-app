import logging
from flask import Blueprint, request
from app.mapping import OrderMap
from app.services import OrderService, UserServices, ProductService, MessageBuilder
from app.mapping import MessageMap

order_bp = Blueprint('order', __name__)
order_map = OrderMap()
order_service = OrderService()
user_service = UserServices()
product_service = ProductService()

@order_bp.route('/orders/<int:id>', methods=['GET'])
def get(id: int):
    order = order_service.find(id) 
    if order:
        message_map, message_finish = message_create(order_map.dump(order, many=False), 'Se encontró el pedido')
        return message_map.dump(message_finish), 200
    else:
        message_map, message_finish = message_create([], f'No se encontró el pedido con ID {id}')
        return message_map.dump(message_finish), 404

@order_bp.route('/orders', methods=['GET'])
def get_all():
    orders = order_service.find_all()
    message_map, message_finish = message_create({'orders': order_map.dump(orders, many=True)}, 'Se encontraron todos los pedidos')
    return message_map.dump(message_finish), 200

@order_bp.route('/orders', methods=['POST'])
def post():
    order_data = request.json
    user = user_service.find(order_data['id_client'])
    if not user:
        message_map, message_finish = message_create([], f'No se encontró el usuario con ID {order_data["id_client"]}')
        return message_map.dump(message_finish), 404

    total_price = 0
    products_to_update = []
    for item in order_data['products']:
        product = product_service.find(item['product_id'])
        if not product:
            message_map, message_finish = message_create([], f'No se encontró el producto con ID {item["product_id"]}')
            return message_map.dump(message_finish), 404
        
        if item['quantity'] <= 0:
            message_map, message_finish = message_create([], f'La cantidad debe ser mayor que 0 para el producto con ID {item["product_id"]}')
            return message_map.dump(message_finish), 400
        
        if product.stock < item['quantity']:
            message_map, message_finish = message_create([], f'Stock insuficiente para el producto con ID {item["product_id"]}')
            return message_map.dump(message_finish), 400
        total_price += product.price * item['quantity']
        products_to_update.append((product, item['quantity']))

    order_data['total'] = total_price

    order = order_map.load(order_data)
    saved_order = order_service.save(order)

    for product, quantity in products_to_update:
        
        product.stock -= quantity
        product_service.save(product)

    message_map, message_finish = message_create(order_map.dump(saved_order, many=False), 'Se creó el pedido')
    return message_map.dump(message_finish), 201

@order_bp.route('/orders/<int:id>', methods=['PUT'])
def update(id: int):
    order = order_service.find(id)
    if not order:
        message_map, message_finish = message_create([], f'No se encontró el pedido con ID {id}')
        return message_map.dump(message_finish), 404
    
    updated_data = request.json

    for key, value in updated_data.items():
        setattr(order, key, value)
    
    order_service.save(order)
    message_map, message_finish = message_create(order_map.dump(order, many=False), f'Se actualizó el pedido con ID {id}')
    return message_map.dump(message_finish), 200

@order_bp.route('/orders/<int:id>', methods=['DELETE'])
def delete(id: int):
    order = order_service.find(id)
    if order:
        order_service.delete(order)
        message_map, message_finish = message_create([], f'Se eliminó el pedido con ID {id}')
        return message_map.dump(message_finish), 200
    else:
        message_map, message_finish = message_create([], f'No se encontró el pedido con ID {id}')
        return message_map.dump(message_finish), 404

@order_bp.route('/orders/user/<int:user_id>', methods=['GET'])
def get_orders_by_user(user_id: int):
    user = user_service.find(user_id)
    if not user:
        message_map, message_finish = message_create([], f'No se encontró el usuario con ID {user_id}')
        return message_map.dump(message_finish), 404

    orders = order_service.find_by_user_id(user_id)
    
    if orders:
        message_map, message_finish = message_create(
            {'orders': order_map.dump(orders, many=True)}, 
            f'Se encontraron los pedidos del usuario con ID {user_id}'
        )
        return message_map.dump(message_finish), 200
    else:
        message_map, message_finish = message_create(
            {'orders': []}, 
            f'No se encontraron pedidos para el usuario con ID {user_id}'
        )
        return message_map.dump(message_finish), 200

def message_create(data, message):
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message(message).add_data(data).build()
    return message_map,message_finish