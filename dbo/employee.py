from dbo.client import db
import datetime
from components.utils.bcrypt import hash_pwd, check_pwd


def db_get_employee(query):
    try:
        employee_details = db.employees.find_one(query)
        if employee_details:
            employee_details['_id'] = str(employee_details['_id'])
            return True, employee_details 
        return False, {
            'message': 'User not found',
            'internal_data': None,
            'status_code': 401
        }
    except Exception as e:
        return False, {
            'message': 'Something went wrong, Please try again later',
            'internal_data': str(e),
            'status_code': 500
        }

def db_employee_register(payload):
    try:
        # status, encrypted_pwd = hash_pwd(payload['password'])
        # if not status:
        #     return status, encrypted_pwd
        data = db.employees.insert_one({
            'emp_id': payload['emp_id'],
            'name': payload['name'],
            'email': payload['email'],
            'mobile': payload['mobile'],
            'role': payload['role'],
            # 'password': encrypted_pwd,
            'status': 'active',
            'created_at': datetime.datetime.now(),
            'deleted_at': None,
            'updated_at': None
        })
        return True, {
            'message': 'User registered successfully and logged in with signup details',
            'internal_data': None,
            'status_code': 200

        }
    except Exception as e:
        return False, {
            'message': 'Something went wrong, Please try again later',
            'internal_data': str(e),
            'status_code': 500
        }
