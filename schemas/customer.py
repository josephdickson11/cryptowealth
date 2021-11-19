from typing import Optional
from pydantic import BaseModel, EmailStr

#attributes required during customer creation
class CustomerCreate(BaseModel):
    username: str
    email : EmailStr
    password : str