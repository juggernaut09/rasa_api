from flask import Flask, send_from_directory
from flask import request as req
from flask import json
from flask import jsonify
from flask import abort
import os


app = Flask(__name__, instance_relative_config=True)
APP_ENV = os.getenv("APP_ENV", "dev")
print(" * APP_ENV : ", APP_ENV)
app.config.from_pyfile(APP_ENV+".py")


@app.route('/')
def app_start():
    resp = jsonify({'message': 'Server is Running.'})
    resp.status_code = 200
    return resp


@app.errorhandler(404)
def not_found_route(error=None):
    message = {
        'status': 'error',
        'message': 'Route Not Found: ' + req.url,
    }

    resp = jsonify(message)
    resp.status_code = 404
    return resp
    
from dbo.client import client
from router.user import bp as user_routes
from router.employee import blueprint as employee_routes
from router.attendance import blueprint as attendance_routes

app.register_blueprint(user_routes)
app.register_blueprint(employee_routes)
app.register_blueprint(attendance_routes)
