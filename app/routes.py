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

@bp.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.get_json() or {}
    # Search for the item
    for item in _items:
        if item['id'] == id:
            # Update its name and return it
            item['name'] = data.get('name', item['name'])
            return jsonify(item), 200
    # If not found, return the error JSON
    return jsonify({'error': 'Not found'}), 404
