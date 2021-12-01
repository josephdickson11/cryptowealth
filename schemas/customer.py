from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr

# attributes required during customer creation
class CustomerCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    referred_by: str


class ShowCustomer(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class UpdateCustomer(BaseModel):
    firstname: str
    lastname: str
    username: str
