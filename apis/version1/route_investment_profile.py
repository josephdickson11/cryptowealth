from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from db.models.customer import Customer
from db.repository.investor_profile import create_new_profile
