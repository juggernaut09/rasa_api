from dbo.employee import db_get_employee, db_employee_register



def get_employee(payload):
    try:
        query = {
            'emp_id': payload['emp_id'],
            # 'email': payload['email'],
            'role': payload['role'],
            'status': 'active'
        }
        status, response = db_get_employee(query)
        return status, response
    except Exception as e:
        return False, {
            'message': 'Something went wrong, Please try again later',
            'internal_data': str(e),
            'status_code': 500
        }

def employee_register(payload):
    try:
        query = {
            'status':'active',
            '$or': [{'emp_id': payload['emp_id']}, {'email': payload['email']}]
        }
        status, response = db_get_employee(query)
        if status:
            return False, {
                'message': "User with the EmployeeId {} or email {} is already existing with the role {}, Please login with your existing credentials".format(response['emp_id'], response['email'], response['role']),
                'internal_data': None,
                'status_code': 409
            }
        status, response = db_employee_register(payload)
        return status, response
    except Exception as e:
        return False, {
            'message': 'Something went wrong, Please try again later',
            'internal_data': str(e),
            'status_code': 500
        }