from flask import Blueprint, request, jsonify
from extensions import db
from models.item import Item
from flask_jwt_extended import jwt_required

item_bp = Blueprint("item_bp", __name__)

@item_bp.route("/", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([item.serialize() for item in items])

@item_bp.route("/", methods=["POST"])
@jwt_required()
def add_item():
    data = request.get_json()
    item = Item(name=data["name"], price=data["price"])
    db.session.add(item)
    db.session.commit()
    return jsonify(item.serialize()), 201
