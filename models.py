from sqlalchemy import Column,Integer,String
from database import base

class Student(base):
    __tablename__="students"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,not_null=True)
    age=Column(Integer)
    gender=Column(String)