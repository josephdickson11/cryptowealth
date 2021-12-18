from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr

# attributes required during customer creation
class CustomerCreate(BaseModel):
    email: EmailStr
    password: str
    pincode: str


class ShowCustomer(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class UpdateCustomer(BaseModel):
    firstname: str
    lastname: str
    username: str


class TokenData(BaseModel):
    email: EmailStr
