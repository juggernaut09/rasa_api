from dbo.employee import db_get_employee
from dbo.attendance import db_check_today_attendance, db_register_attendance
from datetime import datetime
from flask import jsonify


def register_attendance(payload):
    try:
        status, employee_details = db_get_employee({
            'emp_id': payload['emp_id'],
            'role': payload['role'],
            'status': 'active'
        })
        if not status:
            return status, employee_details
        status, attendance_status = db_check_today_attendance({
            'emp_id': employee_details['emp_id'],
            'role': employee_details['role'],
            'status': 'active',
            'month': datetime.utcnow().month,
            'day': datetime.utcnow().day,
            'year': datetime.utcnow().year
        })
        if status:
            return False, {
                'message': 'You have already marked the today\'s attendance',
                'status_code': 409,
                'internal_data': None
            }
        status, attendance_response = db_register_attendance(employee_details)
        return status, attendance_response
    except Exception as e:
        return False, jsonify({
            'message': 'something went wrong, please try again later',
            'internal_data': str(e),
            'status_code': 500
        }), 500