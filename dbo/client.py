from pymongo import MongoClient
from app import app
from instance.dev import MONGODB
client = MongoClient(app.config['MONGODB']['url'], app.config['MONGODB']['port'])
db = client[app.config['MONGODB']['database']]
print(db)