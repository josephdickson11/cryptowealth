from sqlalchemy.orm import Session

from core.hashing import Hasher
from db.models.investor_profile import Investor_profile
from schemas.investor_profile import ProfileCreate
from schemas.investor_profile import UpdateProfile


def create_new_customer(profile: ProfileCreate, db: Session):
    profile = Investor_profile(
        risk_level=profile.risk_level, purpose=profile.invest_purpose
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile


def update_customer(id: int, customer: UpdateProfile, db: Session):
    existing_customer = db.query(Investor_profile).filter(Investor_profile.id == id)
    if not existing_customer.first():
        return 0
    customer.__dict__.update()
    existing_customer.update(customer.__dict__)
    db.commit()
    return 1
