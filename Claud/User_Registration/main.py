from fastapi import FastAPI , HTTPException
from pydantic import BaseModel, EmailStr, validator
from typing import List

app = FastAPI()

class UserCreate(BaseModel):
    username : str
    email :  EmailStr
    password : str
    confirm_password : str
    
    @validator("username")
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be an alphanumeric'
        return v
    
    @validator("confirm_password")
    def password_match(cls, v, values, **kwargs):
        if 'password' in values  and v != values['password']:
            raise ValueError("password is not matching")
        return v
    
class UserOut(BaseModel):
    id : int
    username: str
    email: EmailStr
    
user_db = []

@app.post("/users/", response_model = UserOut)
async def create_user(user: UserCreate):
    if any(u.username == user.username for u in user_db):
        raise HTTPException(status_code= 400, detail= "User already exists")
    if any(u.email== user.email for u in user_db):
        raise HTTPException(status_code=400, detail="Email already exists")
    return  user_db.append(user)

    new_user = UserOut(
        id = len(user_db)+1,
        username = user.username,
        email = user.email
    )
    user_db.append(new_user)
    return new_user

@app.get("/users", response_model = List[UserOut])
async def get_user():
    return user_db