from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crud import (get_users, 
                  create_user, 
                  get_user_by_id,
                  delete_user,
                  update_user_email,
                  get_user_by_name)

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str

class EmailUpdate(BaseModel):
    email: str

@app.get("/")
def home():
    return {"message": "FastAPI is working"}

@app.get("/users")
def read_users(name:str | None = None ):
    if name:
        return get_user_by_name(name)
    return get_users()

@app.post("/users")
def add_user(user: UserCreate):
    created = create_user(
        user.name,
        user.email
    )
    if not created :
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )
    return {"message" : " User Created"}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    found_user = get_user_by_id(user_id)
    if not found_user:
        raise HTTPException(
            status_code= 404,
            detail= "User not found"
        )
    return found_user



@app.put("/users/{user_id}")
def update_user(
    user_id: int,
    user: EmailUpdate
):
    updated = update_user_email(
        user_id,
        user.email
    )
    if not updated:
        raise HTTPException(
            status_code= 404,
            detail= "User not found"
        )
    return{
        "message" : "User updated"
    }

@app.delete("/users/{user_id}")
def remove_user(user_id : int):
    deleted = delete_user(user_id)

    if not deleted:
        raise HTTPException(
            status_code= 404,
            detail = "User not found"
        )
    return {
        "message" : "User deleted"
   }