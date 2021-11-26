from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from db.session import get_db
from db.models.normal_account import Normal_accounts
from schemas.normal_account import AccountCreate, ShowAccount
from db.repository.normal_account import create_new_account

router = APIRouter()


@router.post("/create-account/",response_model=ShowAccount)
def create_account(account: AccountCreate,db: Session = Depends(get_db)):
    current_customer = 1
    account = create_new_account(account=account,db=db,customer_id=current_customer)
    return account
