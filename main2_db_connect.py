from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://monitkk_db_user:3xZ4b73UrpLIMBzZ@mongodb.qxbrzx6.mongodb.net/?appName=MongoDB"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client["users_db"] #db

user_list = db["user_collections"] #collection
