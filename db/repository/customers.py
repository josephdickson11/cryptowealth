from sqlalchemy.orm import Session

from core.hashing import Hasher
from db.models.customer import Customer
from schemas.customer import CustomerCreate
from schemas.customer import UpdateCustomer


def create_new_customer(customer: CustomerCreate, db: Session):
    customer = Customer(
        email=customer.email,
        hashed_password=Hasher.get_password_hash(customer.password),
        is_KYC=False,
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer


def update_customer(id: int, customer: UpdateCustomer, db: Session):
    existing_customer = db.query(Customer).filter(Customer.id == id)
    if not existing_customer.first():
        return 0
    customer.__dict__.update()
    existing_customer.update(customer.__dict__)
    db.commit()
    return 1
