from model.todos import Students
from pydantic import BaseModel
from typing import List


class StudentCollection(BaseModel):

    students: List[Students]
