from sqlalchemy.orm import Session

from db.models.customer import Customer


def get_customer(username: str, db: Session):
    customer = db.query(Customer).filter(Customer.email == username).first()
    return customer
