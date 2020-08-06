import bcrypt

def hash_pwd(password):
    try:
        hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return True, hashed_pwd

    except Exception as e :
        return False, {
            'message': "Something went wrong Please, try again later.",
            'status_code': 500,
            'internal_data': str(e)
        }


def check_pwd(password, hashed):
    try:
        if bcrypt.checkpw(password.encode('utf-8'), hashed):
            return True, {
                'message': 'Valid password',
                'status_code': 200,
                'internal_data': None
            }
        return False, {
            'message': 'Invalid password',
            'status_code': 401,
            'internal_data': None
        }
    except Exception as e :
        return False, {
            'message': "Something went wrong Please, try again later.",
            'status_code': 500,
            'internal_data': str(e)
        }