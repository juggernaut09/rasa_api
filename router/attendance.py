from flask import jsonify, request, Blueprint
from components.attendance import register_attendance, get_present_month_analysis

blueprint = Blueprint('attendance_blueprint', __name__)


@blueprint.route('/mark/attendance', methods=['POST'])
def mark_attendance():
    try:
        payload = request.get_json()
        status, response = register_attendance(payload)
        return jsonify(response), response['status_code']
    except Exception as e:
        return jsonify({
            'message': 'something went wrong, please try again later',
            'internal_data': str(e),
            'status_code': 500
        }), 500


@blueprint.route('/present_month/analysis', methods=['GET'])
def present_month_analysis():
    try:
        args = request.args
        if (not ('role' in args)) or (not ('emp_id' in args)):
            return jsonify({
            'status_code': 400,
            'message': 'Invalid query params',
            'internal_data': None
            })
        payload = {
        'role': args['role'],
        'emp_id': args['emp_id']
        }
        status, response = get_present_month_analysis(payload)
        if status:
            return jsonify(response), 200
        return jsonify(response), response['status_code']
    except Exception as e:
        return jsonify({
            'message': 'something went wrong, please try again later',
            'internal_data': str(e),
            'status_code': 500
        }), 500
