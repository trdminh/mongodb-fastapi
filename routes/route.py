from fastapi import APIRouter
from model.todos import Todo
from config.database import collection_name
from schema.schema import list_serial
from bson import ObjectId

router = APIRouter()

@router.get('/')
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos

@router.post('/')
async def post_todos(todo: Todo):
    collection_name.insert_one(dict(todo))
    
@router.put('/{id}')
async def put_todos(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    
@router.delete('/{id}')
async def delete_todos(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})