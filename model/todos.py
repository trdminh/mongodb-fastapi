from pydantic  import BaseModel, EmailStr, Field, ConfigDict
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
from bson import ObjectId
from typing import Optional, List

PyObjectId = Annotated[str, BeforeValidator(str)]

class Students(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field()
    email: EmailStr = Field()
    course: str = Field()
    gpa: float = Field(le=4.0)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Minh",
                "email": "doanminh750@gmail.com",
                "course": "MongoDB Tutorial",
                "gpa": 3.0,
            }
        },
    )

class UpdateStudent(BaseModel):
    name  : Optional[str] = None
    email : Optional[EmailStr] = None
    course: Optional[str] = None
    gpa   : Optional[float] = None
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Minh",
                "email": "doanminh750@gmail.com",
                "course": "MongoDB Tutorial",
                "gpa": 3.0,
            }
        },
    )

