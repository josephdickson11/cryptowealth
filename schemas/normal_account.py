from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime

#shared properties
class AccountBase(BaseModel):
    
    