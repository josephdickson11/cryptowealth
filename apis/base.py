from fastapi import APIRouter
from sqlalchemy.ext.declarative import api

from apis.version1 import route_general_pages
from apis.version1 import route_customers

api_router = APIRouter()
api_router.include_router(route_general_pages.general_pages_router, prefix="", tags=["general_pages"])
api_router.include_router(route_customers.router, prefix="/customers", tags=["customers"])