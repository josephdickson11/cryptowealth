from sqlalchemy.orm import Session

from schemas.customer import CustomerCreate
from db.models.customer import Customer
from core.hashing import Hasher

def create_new_customer(customer: CustomerCreate, db:Session):
    customer = Customer(
        username = customer.username,
        email = customer.email,
        hashed_password = Hasher.get_password_hash(customer.password),
        is_KYC = False,
        referred_by = customer.referred_by
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer