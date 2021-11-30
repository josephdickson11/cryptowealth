from sqlalchemy.orm import Session

from schemas.normal_account import AccountCreate
from db.models.normal_account import Normal_accounts


def create_new_account(account: AccountCreate, db: Session, customer_id:int):
    account_obj = Normal_accounts(**account.dict(), customer_id=customer_id)
    db.add(account_obj)
    db.commit()
    db.refresh(account_obj)
    return account_obj

def retrieve_account(id:int, db:Session):
    item = db.query(Normal_accounts).filter(Normal_accounts.id == id).first()
    return item