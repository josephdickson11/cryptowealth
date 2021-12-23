from fastapi import Depends
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy.orm import Session

from core.security import get_authentic_customer
from db.models.customer import Customer
from db.session import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login/token/")


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    return get_authentic_customer(db, token)
