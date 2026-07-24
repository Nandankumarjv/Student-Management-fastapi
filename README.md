# 🎓 Student Management API

A RESTful Student Management API built using **FastAPI**, **SQLAlchemy**, and **SQLite**. This project demonstrates CRUD (Create, Read, Update, Delete) operations with request validation using Pydantic and database integration using SQLAlchemy ORM.

---

## 🚀 Features

- Create a new student
- Get all students
- Get student by ID
- Update student details
- Delete a student
- Request validation using Pydantic
- Database integration using SQLite
- SQLAlchemy ORM
- Automatic API documentation using Swagger UI

---

## 🛠️ Tech Stack

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/student-management-fastapi.git
```

### Move into the project

```bash
cd student-management-fastapi
```

### Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
uvicorn main:app --reload
```

---

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 📥 Example Request

```json
{
    "id": 1,
    "name": "Alice",
    "age": 20,
    "gender": "F"
}
```

---

## 📤 Example Response

```json
{
    "id": 1,
    "name": "Alice",
    "age": 20,
    "gender": "F"
}
```

---

## 📚 Concepts Learned

- REST API Development
- CRUD Operations
- FastAPI Routing
- Dependency Injection
- Pydantic Validation
- SQLAlchemy ORM
- SQLite Database
- HTTP Status Codes
- Error Handling with HTTPException

---

## 🔮 Future Improvements

- JWT Authentication
- Password Hashing
- APIRouter
- Pagination
- Search & Filtering
- Environment Variables (.env)
- Alembic Migrations
- Unit Testing
- Docker Support