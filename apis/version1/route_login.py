from datetime import timedelta

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import false
from typing_extensions import runtime

from core.config import settings
from core.hashing import Hasher
from core.security import create_access_token
from db.models.customer import Customer
from db.repository.login import get_customer
from db.session import get_db
from schemas.tokens import Token

router = APIRouter()


def authenticate_customer(username: str, password: str, db: Session):
    customer = get_customer(username=username, db=db)
    print(customer)
    if not customer:
        return False
    if not Hasher.verify_password(password, customer.hashed_password):
        return False
    return customer


@router.post("/", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    customer = authenticate_customer(form_data.username, form_data.password, db)
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password"
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": customer.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}