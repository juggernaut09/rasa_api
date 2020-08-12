from flask import jsonify, request, Blueprint
from components.attendance import register_attendance, get_year_analysis, get_month_analysis, get_day_analysis

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


@blueprint.route('/year/analysis', methods=['POST'])
def year_analysis():
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
        'emp_id': args['emp_id'],
        'year': request.get_json()['year']
        }
        status, response = get_year_analysis(payload)
        if status:
            return jsonify(response), 200
        return jsonify(response), response['status_code']
    except Exception as e:
        return jsonify({
            'message': 'something went wrong, please try again later',
            'internal_data': str(e),
            'status_code': 500
        }), 500

@blueprint.route('/month/analysis', methods=['POST'])
def month_analysis():
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
        'emp_id': args['emp_id'],
        'month': request.get_json()['month'],
        'year': request.get_json()['year']
        }
        status, response = get_month_analysis(payload)
        if status:
            return jsonify(response), 200
        return jsonify(response), response['status_code']
    except Exception as e:
        return jsonify({
            'message': 'something went wrong, please try again later',
            'internal_data': str(e),
            'status_code': 500
        }), 500

@blueprint.route('/day/analysis', methods=['POST'])
def today_analysis():
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
        'emp_id': args['emp_id'],
        'day': request.get_json()['day'],
        'month': request.get_json()['month'],
        'year': request.get_json()['year']
        }
        status, response = get_day_analysis(payload)
        if status:
            return jsonify(response), 200
        return jsonify(response), response['status_code']
    except Exception as e:
        return jsonify({
            'message': 'something went wrong, please try again later',
            'internal_data': str(e),
            'status_code': 500
        }), 500
