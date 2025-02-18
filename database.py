from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")
MONGODB_URL = config.get("MONGODB_URL")

client = MongoClient(MONGODB_URL, tls=True, tlsAllowInvalidCertificates=True)  
db = client["myDataBase"]
collection = db["users"]
collection.create_index("email", unique=True)
