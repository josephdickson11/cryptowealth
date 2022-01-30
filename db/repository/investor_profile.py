from sqlalchemy.orm import Session

from core.hashing import Hasher
from db.models.investor_profile import Investor_profile
from schemas.investor_profile import ProfileCreate
from schemas.investor_profile import UpdateProfile


def create_new_profile(profile: ProfileCreate, db: Session, customer_id: int):
    profile = Investor_profile(**profile.dict(), customer_id=customer_id)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile


def retrieve_profile(id: int, db: Session):
    item = db.query(Investor_profile).filter(Investor_profile.id == id).first()
    return item


def update_profile(id: int, customer: UpdateProfile, db: Session):
    existing_customer = db.query(Investor_profile).filter(Investor_profile.id == id)
    if not existing_customer.first():
        return 0
    customer.__dict__.update()
    existing_customer.update(customer.__dict__)
    db.commit()
    return 1
