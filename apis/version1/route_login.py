from datetime import timedelta

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import false
from typing_extensions import runtime

from core.config import settings
from core.hashing import Hasher
from core.helper import get_customer_by_mail
from core.security import create_access_token
from core.security import get_authentic_customer
from db.models.customer import Customer
from db.repository.login import get_current_user
from db.session import get_db
from schemas.customer import ShowCustomer
from schemas.tokens import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token", auto_error=False)

router = APIRouter()


def authenticate_customer(username: str, password: str, db: Session):
    customer = get_customer_by_mail(username=username, db=db)
    print(customer)
    if not customer:
        return False
    if not Hasher.verify_password(password, customer.hashed_password):
        return False
    return customer


@router.post("/authenticate")
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
    customer_obj = {
        "id": customer.id,
        "firstname": customer.firstname,
        "email": customer.email,
        "total_account": customer.total_account,
        "referral_id": customer.referral_id,
        "lastname": customer.lastname,
        "is_KYC": customer.is_KYC,
        "referred_by": customer.referred_by,
        "isEmailVerified": customer.is_verified,
    }

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "userdict": customer_obj,
    }


@router.post("/userdata")
def read_logged_in_user(current_user=Depends(get_current_user)):
    return current_user
