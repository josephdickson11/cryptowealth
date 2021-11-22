from typing import Optional
from pydantic import BaseModel, EmailStr

#attributes required during customer creation
class CustomerCreate(BaseModel):
    username: str
    email : EmailStr
    password : str


class ShowCustomer(BaseModel):
    username: str
    email: EmailStr

    class Config():
        orm_mode = True