from dbo.employee import db_get_employee
from dbo.attendance import db_check_today_attendance, db_register_attendance, db_get_attendance_analysis
from datetime import datetime
from flask import jsonify
from app import app
import json, pandas, os
from pandas.io.json import json_normalize
from json_excel_converter import Converter
from json_excel_converter.xlsx import Writer


def register_attendance(payload):
    try:
        # if (datetime.now() > datetime.now().replace(hour=11, minute=0, second=0, microsecond=0)):
        #     return False, {
        #         'message': 'You can mark attendance before 11 AM',
        #         'status_code': 400,
        #         'internal_data': None
        #     }
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
            'month': datetime.now().month,
            'day': datetime.now().day,
            'year': datetime.now().year
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

def get_year_analysis(payload):
    try:
        if payload["role"] != "admin":
            return False, {
            'message': 'You are not authorized to do this action',
            'status_code': 401,
            'internal_data': None
            }
        status, employee_details = db_get_employee({
            'emp_id': payload['emp_id'],
            'role': payload['role'],
            'status': 'active'
        })
        if not status:
            return status, employee_details
        status, response = db_get_attendance_analysis(query= {
                                                        'year': int(payload['year']),
                                                        'status': 'active',
                                                        })
        if status:
            xlsx_path = os.path.join('static', 'xlsx', 'data.xlsx')
            conv = Converter()
            conv.convert(response, Writer(file=xlsx_path))
            return True, {
                "url": '{}/{}'.format(app.config['HOST']['url'], xlsx_path)
                }
        return False, response
    except Exception as e:
        return False, jsonify({
            'message': 'something went wrong, please try again later',
            'internal_data': str(e),
            'status_code': 500
        }), 500

def get_month_analysis(payload):
    try:
        if payload["role"] != "admin":
            return False, {
            'message': 'You are not authorized to do this action',
            'status_code': 401,
            'internal_data': None
            }
        status, employee_details = db_get_employee({
            'emp_id': payload['emp_id'],
            'role': payload['role'],
            'status': 'active'
        })
        if not status:
            return status, employee_details
        print('month : '.format(payload['month']))
        status, response = db_get_attendance_analysis(query= {
                                                        'month': int(payload["month"]),
                                                        'year': int(payload['year']),
                                                        'status': 'active',
                                                        })
        if status:
            xlsx_path = os.path.join('static', 'xlsx', 'data.xlsx')
            conv = Converter()
            conv.convert(response, Writer(file=xlsx_path))
            return True, {
                "url": '{}/{}'.format(app.config['HOST']['url'], xlsx_path)
                }
        return False, response
    except Exception as e:
        return False, jsonify({
            'message': 'something went wrong, please try again later',
            'internal_data': str(e),
            'status_code': 500
        }), 500


def get_day_analysis(payload):
    try:
        if payload["role"] != "admin":
            return False, {
            'message': 'You are not authorized to do this action',
            'status_code': 401,
            'internal_data': None
            }
        status, employee_details = db_get_employee({
            'emp_id': payload['emp_id'],
            'role': payload['role'],
            'status': 'active'
        })
        if not status:
            return status, employee_details
        status, response = db_get_attendance_analysis(query= {
                                                        'month': int(payload["month"]),
                                                        'day': int(payload['day']),
                                                        'status': 'active',
                                                        'year': int(payload['year'])
                                                        })
        # print('response : {}'.format(response))
        if status:
            xlsx_path = os.path.join('static', 'xlsx', 'data.xlsx')
            conv = Converter()
            conv.convert(response, Writer(file=xlsx_path))
            return True, {
                "url": '{}/{}'.format(app.config['HOST']['url'], xlsx_path)
                }
        return False, response
    except Exception as e:
        return False, jsonify({
            'message': 'something went wrong, please try again later',
            'internal_data': str(e),
            'status_code': 500
        }), 500
