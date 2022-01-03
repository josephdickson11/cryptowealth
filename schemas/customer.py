from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr

from db.base_class import Base

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


class TokenData(BaseModel):
    email: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class UserProfilr(BaseModel):
    access_token: str
    token_type: str
    email: EmailStr
