from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr

from db.base_class import Base

# attributes required during customer creation
class ProfileCreate(BaseModel):
    risk_level: str
    invest_purpose: str


class ShowProfile(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class UpdateProfile(BaseModel):
    firstname: str
    lastname: str


class UserProfile(BaseModel):
    access_token: str
    token_type: str
    email: EmailStr
