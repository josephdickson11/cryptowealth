from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr

from db.base_class import Base

# attributes required during customer creation
class ProfileCreate(BaseModel):
    risk_level: str
    invest_purpose: str


class ShowProfile(BaseModel):
    risk_level: str

    class Config:
        orm_mode = True


class UpdateProfile(BaseModel):
    risk_level: str
    invest_purpose: str


class UserProfile(BaseModel):
    access_token: str
    token_type: str
    email: EmailStr
