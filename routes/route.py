from fastapi import APIRouter, HTTPException, Body, status
from fastapi.responses import Response
from pymongo import ReturnDocument
from model.todos import Students, UpdateStudent
from config.connection import student_collection
from schema.schema import StudentCollection
from bson import ObjectId


router = APIRouter()

@router.get('/student',
            response_description="List all students",
            response_model=StudentCollection,
            response_model_by_alias=False
        )
async def list_students():

    return StudentCollection(students=await student_collection.find().to_list(1000))


@router.get(
    '/student/{student_id}',
    response_description="Get student by id",
    response_model=Students,
    response_model_by_alias=False
)
async def show_student(student_id):
    if (
        student := await student_collection.find_one({"_id": ObjectId(id)})
    ) is not None:
        return student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")

@router.post(
    '/student',
    response_description="Add new student",
    response_model=Students,
    response_model_by_alias=False
)
async def create_student(student: Students = Body(...)):
    new_student = await student_collection.insert_one(
        student.model_dump(by_alias=True,exclude=['id'] )
    )
    create_student = await student_collection.find_one(
         {"_id": new_student.inserted_id}
    )
    return create_student

@router.put(
    '/student/{id}',
    response_description="Update student",
    response_model=Students,
    response_model_by_alias=False
)
async def update_student(id: str, student: UpdateStudent = Body(...)):
    student = {
        k: v for k, v in student.model_dump(by_alias=True).items() if v is not None
    }
    if len(student) >= 1:
        update_result = await student_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": student},
            return_document=ReturnDocument.AFTER,
        )
        if update_result is not None:
            return update_result
        else:
            raise HTTPException(status_code=404, detail=f"Student {id} not found")

    # The update is empty, but we should still return the matching document:
    if (existing_student := await student_collection.find_one({"_id": id})) is not None:
        return existing_student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")

@router.delete(
    '/student/{id}',
    response_description="Delete a student"
)
async def delete_student(id: str):
    delete_result = await student_collection.delete_one({"_id": ObjectId(id)})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Student {id} not found")