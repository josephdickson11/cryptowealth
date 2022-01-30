from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from db.models.customer import Customer
from db.repository.investor_profile import create_new_profile
from db.repository.investor_profile import list_profiles
from db.repository.investor_profile import retrieve_profile
from db.repository.investor_profile import update_profile
from db.session import get_db
from schemas.investor_profile import ProfileCreate
from schemas.investor_profile import ShowProfile
from schemas.investor_profile import UpdateProfile

router = APIRouter()


@router.post("/create-investment-profile", response_model=ShowProfile)
def create_investment_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    current_customer = db.query(Customer.id).first()
    formatted_id = current_customer[0]
    profile = create_new_profile(profile=profile, db=db, customer_id=formatted_id)
    return profile


@router.get("/get/{id}", response_model=ShowProfile)
def read_investment_profile(id: int, db: Session = Depends(get_db)):
    profile = retrieve_profile(id=id, db=db)
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"account with id {id} does not exist",
        )
    return profile


@router.get("/all", response_model=List[ShowProfile])
def read_investment_profiles(db: Session = Depends(get_db)):
    profiles = list_profiles(db=db)
    return profiles


@router.post("/update/{id}")
def update_profile(id: int, profile: UpdateProfile, db: Session = Depends(get_db)):
    message = update_profile(id=id, profile=profile, db=db)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"profile with id {id} not found",
        )
    return {"msg": "Successfully updated data."}
