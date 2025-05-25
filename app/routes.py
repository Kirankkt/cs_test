from flask import Blueprint, jsonify, request

bp = Blueprint('main', __name__)

# Simple in-memory “database”
_items = []

@bp.route('/items', methods=['GET'])
def list_items():
    return jsonify(_items), 200

@bp.route('/items', methods=['POST'])
def add_item():
    data = request.get_json() or {}
    item = {'id': len(_items) + 1, 'name': data.get('name', '')}
    _items.append(item)
    return jsonify(item), 201
