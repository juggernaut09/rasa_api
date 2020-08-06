from flask import Blueprint
from flask import jsonify
bp=Blueprint('users',__name__)

@bp.route('/signup', methods=['POST'])
def signup():
    return jsonify({'message': 'Hello'})
