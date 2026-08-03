from pydantic import BaseModel, EmailStr
from datetime import datetime


#Data coming from client during resitration
class UserCreate(BaseModel):
    email:EmailStr
    password:str



#Data returned to the Client
class UserResponse(BaseModel):
    id:int
    email:EmailStr
    is_active:bool
    created_at:datetime

    class config:
        from_attributes=True

# Data used during login
class UserLogin(BaseModel):

    email: EmailStr
    password: str        

