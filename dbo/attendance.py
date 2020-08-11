from dbo.client import db
from datetime import datetime
from bson import objectid


def db_register_attendance(employee_details):
    try:
        response = db.attendance.insert_one({
            'emp_id': employee_details['emp_id'],
            'role': employee_details['role'],
            'name': employee_details['name'],
            'month': datetime.now().month,
            'day': datetime.now().day,
            'year': datetime.now().year,
            'time': "{}:{}:{}".format(datetime.now().hour, datetime.now().minute, datetime.now().second),
            'created_at': datetime.now(),
            'attendance': 'present',
            'status': 'active',
            'deleted_at': None,
            'updated_at': None
        })
        if response:
            return_response = db.attendance.find_one({
                '_id': response.inserted_id,
                'status': 'active'
            })
            if return_response:
                return True, {
                    'message': 'Successfully registered your attendance',
                    'status_code': 200,
                    'internal_data': None
                }
        return False, {
            'message': 'Something went wrong, Please try again later',
            'internal_data': None,
            'status_code': 500
        }
    except Exception as e:
        return False, {
            'message': 'Something went wrong, Please try again later',
            'internal_data': str(e),
            'status_code': 500
        }


def db_check_today_attendance(query):
    try:
        response = db.attendance.find_one(query)
        if response:
            response['_id'] = str(response['_id'])
            return True, response
        return False, {
            'message': 'You have not marked the attendance today',
            'internal_data': None,
            'status_code': 400
        }
    except Exception as e:
        return False, {
            'message': 'Something went wrong, Please try again later',
            'internal_data': str(e),
            'status_code': 500
        }

def db_get_attendance_analysis(query):
    try:
        response = list(db.attendance.find(query))
        if len(response):
            for resp in response:
                resp.pop('_id')
                if 'created_at' in resp:
                    resp.pop('created_at')
                resp.pop('deleted_at')
                resp.pop('updated_at')
                resp.pop('status')
            return True, response
        return False, {
        'message': 'There is no details to show.',
        'status_code': 400,
        'internal_data': None
        }
    except Exception as e:
        return False, {
            'message': 'Something went wrong, Please try again later',
            'internal_data': str(e),
            'status_code': 500
        }
