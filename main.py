from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import sessionLocal,engine
from pydantic import BaseModel
models.base.metadata.create_all(bind=engine)
app=FastAPI()

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students")
def create_student(student:schemas.createStudent,
                    db:Session=Depends(get_db)):

    new_student=models.Student(
        id=student.id,
        name=student.name,
        age=student.age,
        gender=student.gender)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/students",response_model=list[schemas.responseStudent])
def get_details(db:Session=Depends(get_db)):
    students=db.query(models.Student).all()
    return students

@app.get("/students/{id}",response_model=schemas.responseStudent)
def details_by_id(id:int,db:Session=Depends(get_db)):
        student=db.query(models.Student).filter(models.Student.id==id).first()
        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Not found"
            )
        return student
   
@app.put("/students/{id}",response_model=schemas.updateStudent)
def update_student(id:int,student:schemas.updateStudent,db:Session=Depends(get_db)):
    db_student=db.query(models.Student).filter(models.Student.id==id).first()
    if db_student is None:
        raise HTTPException(
            status_code=404,
            detail="Not found"
        )
    db_student.name=student.name
    db_student.age=student.age
    db_student.gender=student.gender

    db.commit()
    db.refresh(db_student)
    return db_student

@app.delete("/students/{id}")
def remove(id:int,db:Session=Depends(get_db)):
    remove_student=db.query(models.Student).filter(models.Student.id==id).first()
    if remove_student is None:
        raise HTTPException(
            status_code=404,
            detail="Not found"
        )
    db.delete(remove_student)
    db.commit()
    return {
        "Message":"Student deleted successfully"
    }
