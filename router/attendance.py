from flask import jsonify, request, Blueprint
from components.attendance import register_attendance

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