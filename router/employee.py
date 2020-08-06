from flask import Blueprint, request, jsonify
from components.employee import get_employee, employee_register

blueprint = Blueprint('employee_blueprint',__name__)

@blueprint.route('/employee/signin', methods=['POST'])
def employee_signin():
    payload = request.get_json()
    status, response = get_employee(payload)
    if status:
        return jsonify(response), 200
    return jsonify(response), response['status_code']


@blueprint.route('/employee/signup', methods=['POST'])
def employee_signup():
    payload = request.get_json()
    status, response = employee_register(payload)
    if status:
        return jsonify(response), 200
    return jsonify(response), response['status_code']