import json
from typing import List 
from pydantic import BaseModel
from fastapi import FastAPI,Request
from starlette.responses import Response, JSONResponse



app = FastAPI()

@app.get("/hello")
def say_hello():
 return JSONResponse(
            content={"message": "Hello, world!"},
            status_code = 200
        ) 

@app.get("/welcome")
def read_hello(request: Request): 
    names = request.headers.get("name") 
    if names == "str":
        return JSONResponse(
            content={"Welcome": "Soa"},
            status_code = 200
        ) 
        
class Students(BaseModel):
    Reference: str 
    firstName: str 
    LastName: str 
    age: int
    
students: List[Students] = []
def classMate(): 
    student_converted = [ {"Reference": "STD24156",
     "firstName": "Soa",
     "LstName": "Rakoto",
     "age": 16}] 
    
    for student in students: 
        student_converted.append(student.model_dump()) 
    return student_converted

@app.post("/students")
def add_students(new_students: 
    List[Students]): 
    students.extend(new_students)
    return{"students":
classMate()}
    
    
@app.get("/students")
def list_students(): 
    return JSONResponse(
            content={"students": classMate()},
            status_code = 200
        ) 

@app.put("/students")
def update_students(students: List[Students]):
    for new_student in students:
        found = False
        for i, existing_student in enumerate(students):
            if existing_student.Reference == new_student.Reference: 
                students[i] = new_student
                found = True
                break
        if not found:
           students.append(new_student)
    return {"students": classMate()}



   