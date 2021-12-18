from fastapi import Depends
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy.orm import Session

from core.security import decode_access_token
from db.models.customer import Customer
from db.session import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def get_customer(username: str, db: Session):
    customer = db.query(Customer).filter(Customer.email == username).first()
    return customer


async def get_current_customer(token: str = Depends(oauth2_scheme)):
    return "testing"


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    return decode_access_token(db, token)
