import logging
from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from app.mapping import UserMap
from app.services import UserServices
from app.mapping import MessageMap
from app.services import MessageBuilder, Message

user_bp = Blueprint('user', __name__)
user_map = UserMap()
user_service = UserServices()

@user_bp.route('/users/<int:id>', methods=['GET'])
def get(id: int):
    logging.info(f'Usuario ID: {id}')
    user = user_service.find(id)
    message_map, message_finish = message_create(user_map.dump(user, many=False), 'Se encontro el usuario')
    return message_map.dump(message_finish), 200

@user_bp.route('/users', methods=['GET'])
def get_all():
    users = user_service.find_all()
    message_map, message_finish = message_create({'users': user_map.dump(users, many=True)}, 'Se encontro todos los usuarios')
    return message_map.dump(message_finish), 200

@user_bp.route('/users', methods=['POST'])
def post():
    user = user_map.load(request.json)
    user_service.save(user)
    logging.info(f'Usuario: {user}')
    message_map, message_finish = message_create(user_map.dump(user), 'Usuario Creado')
    return message_map.dump(message_finish), 201


@user_bp.route('/users/<int:id>', methods=['PUT'])
def update(id: int):
    user = user_service.find(id)
    if not user:
        message_map, message_finish = message_create({}, f'Usuario con ID {id} no encontrado')
        return message_map.dump(message_finish), 404

    updated_data = request.json
    
    for key, value in updated_data.items():
        setattr(user, key, value)
    
    updated_user = user_service.save(user)
    
    message_map, message_finish = message_create(user_map.dump(updated_user), f'Usuario con ID {id} Actualizado')
    return message_map.dump(message_finish), 200

@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete(id: int):
    user = user_service.find(id)
    if user:
        user_service.delete(user)
        message_map, message_finish = message_create([], f'Usuario con ID {id} Eliminado')
        return message_map.dump(message_finish), 200
    else:
        message_map, message_finish = message_create([], f'Usuario con ID {id} no encontrado')
        return message_map.dump(message_finish), 404

def message_create(data, message):
    message_map = MessageMap()
    message_builder = MessageBuilder()
    message_finish = message_builder.add_message(message).add_data(data).build()
    return message_map,message_finish