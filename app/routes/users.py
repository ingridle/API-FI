from flask import Blueprint, request, abort
from ..schemas.user_schema import UserSchema
from ..controllers import user_controller

users_bp = Blueprint("users", __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@users_bp.route("/users", methods=["GET"])
def get_users():
    users = user_controller.listar_usuarios()
    return users_schema.jsonify(users), 200

@users_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_controller.obter_usuario(user_id)
    if not user:
        abort(404, description="Usuário não encontrado.")
    return user_schema.jsonify(user), 200

@users_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    validated = user_schema.load(data)
    novo = user_controller.criar_usuario(validated)
    return user_schema.jsonify(novo), 201

@users_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = user_controller.obter_usuario(user_id)
    if not user:
        abort(404)
    data = request.get_json()
    validated = user_schema.load(data)
    atualizado = user_controller.atualizar_usuario(user, validated)
    return user_schema.jsonify(atualizado), 200

@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = user_controller.obter_usuario(user_id)
    if not user:
        abort(404)
    user_controller.deletar_usuario(user)
    return '', 204