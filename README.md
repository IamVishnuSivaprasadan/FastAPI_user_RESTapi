# FastAPI PostgreSQL User Management API

A RESTful User Management API built with **FastAPI** and **PostgreSQL**.

This project demonstrates backend development fundamentals including API design, database integration, request validation, error handling, and interactive API documentation.

---

## Features

* Create a user
* Retrieve all users
* Retrieve a user by ID
* Search users by name
* Update user email
* Delete a user
* PostgreSQL database integration
* Request validation using Pydantic
* HTTP status code handling
* Interactive Swagger documentation

---

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* Psycopg
* Pydantic
* Uvicorn
* Python Dotenv

---

## Project Structure

```text
FastAPI_user_RESTapi/
│
├── main.py
├── crud.py
├── database.py
├── .env
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Get All Users

```http
GET /users
```

### Get User By ID

```http
GET /users/{user_id}
```

### Create User

```http
POST /users
```

Request Body:

```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

### Update User Email

```http
PUT /user/{user_id}
```

Request Body:

```json
{
  "email": "newemail@example.com"
}
```

### Delete User

```http
DELETE /users/{user_id}
```

---

## Database Configuration

Create a `.env` file:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd fastapi_user_api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn main:app --reload
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Status Codes

| Code | Description        |
| ---- | ------------------ |
| 200  | Successful Request |
| 400  | Bad Request        |
| 404  | Resource Not Found |
| 422  | Validation Error   |

---

## Learning Outcomes

This project helped reinforce:

* REST API principles
* HTTP methods (GET, POST, PUT, DELETE)
* Path parameters
* Request validation
* Exception handling
* PostgreSQL integration
* API testing with Swagger
* Backend project structure

---

## Future Improvements

* JWT Authentication
* User Search Endpoint
* Pagination
* Filtering
* SQLAlchemy ORM
* Docker Support
* Automated Testing with Pytest
* Deployment to Render or Railway

---

## Author

Vishnu Sivaprasadan
Built as part of a backend engineering and full-stack development learning journey using Python, FastAPI, PostgreSQL, and React.
