from pydantic import BaseModel,ConfigDict

class createStudent(BaseModel):
    id:int
    name:str
    age:int
    gender:str

class responseStudent(BaseModel):
    id:int
    name:str
    age:int
    gender:str

    model_config=ConfigDict(from_attributes=True)

class updateStudent(BaseModel):
    name:str
    age:int
    gender:str

