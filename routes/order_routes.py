from flask import Blueprint, request, jsonify
from app import db
from models.order import Order
from flask_jwt_extended import jwt_required, get_jwt_identity

order_bp = Blueprint('orders', __name__, url_prefix='/orders')

@order_bp.route('/', methods=['POST'])
@jwt_required()
def place_order():
    data = request.json
    user_id = get_jwt_identity()
    item_id = data.get('item_id')
    quantity = data.get('quantity')

    if not item_id or not quantity:
        return jsonify({"msg": "Item ID and quantity required"}), 400

    order = Order(user_id=user_id, item_id=item_id, quantity=quantity)
    db.session.add(order)
    db.session.commit()

    return jsonify({"msg": "Order placed", "order_id": order.id}), 201

@order_bp.route('/', methods=['GET'])
@jwt_required()
def get_orders():
    user_id = get_jwt_identity()
    orders = Order.query.filter_by(user_id=user_id).all()
    result = [{"id": o.id, "item_id": o.item_id, "quantity": o.quantity} for o in orders]
    return jsonify(result)
