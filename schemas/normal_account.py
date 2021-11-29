from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime

#shared properties
class AccountBase(BaseModel):
    wallet_address : Optional[str] = None
    date_created : Optional[date] = datetime.now().date()


class AccountCreate(AccountBase):
    wallet_address: str


class ShowAccount(AccountBase):
    wallet_address : str
    date_created : date

    class Config():
        orm_mode = True
