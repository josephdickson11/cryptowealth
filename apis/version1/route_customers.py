from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from db.repository.customers import create_new_customer
from db.repository.customers import update_customer
from db.session import get_db
from schemas.customer import CustomerCreate
from schemas.customer import ShowCustomer
from schemas.customer import UpdateCustomer

# from starlette.types import Message

router = APIRouter()


@router.post("/", response_model=ShowCustomer)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    customer = create_new_customer(customer=customer, db=db)
    return customer


@router.post("/update/{id}")
def update_customer_(id: int, customer: UpdateCustomer, db: Session = Depends(get_db)):
    message = update_customer(id=id, customer=customer, db=db)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"customer with id {id} not found",
        )
    return {"msg": "Successfully updated data."}
