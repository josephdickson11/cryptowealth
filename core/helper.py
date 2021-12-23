from pydantic import EmailStr
from sqlalchemy.orm import Session

from db.models.customer import Customer


def get_customer_id(id: int, db: Session):
    customer = db.query(Customer).filter(Customer.id == id).first()
    return customer


def get_customer(db: Session, email: str):
    if email in db:
        user_dict = db[email]
        return Customer(**user_dict)


def get_customer_by_mail(username: str, db: Session):
    customer = db.query(Customer).filter(Customer.email == username).first()
    return customer
