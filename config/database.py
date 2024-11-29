from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
user: str = 'minh'
password: str = '123'
host: str = 'cluster0.kkfs0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
url: str = f'mongodb+srv://{user}:{password}@{host}'
    
client = AsyncIOMotorClient(url)

db = client.todo_db
collection_name = db["collection_name"]