from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field


app = FastAPI(title="Student Management API")


class Student(BaseModel):
    name: str
    age: int = Field(ge=18, le=30)
    email: EmailStr
    course: str


students = {
    1: {
        "id": 1,
        "name": "Kartik",
        "age": 21,
        "email": "kartik@example.com",
        "course": "ECE"
    }
}


@app.get("/students")
def get_students():
    return list(students.values())


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    return students[student_id]


@app.post("/students", status_code=201)
def create_student(student: Student):
    new_id = max(students.keys()) + 1

    new_student = {
        "id": new_id,
        **student.model_dump()
    }

    students[new_id] = new_student

    return new_student


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    updated_student = {
        "id": student_id,
        **student.model_dump()
    }

    students[student_id] = updated_student

    return updated_student


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    del students[student_id]

    return {"message": "Student deleted successfully"}