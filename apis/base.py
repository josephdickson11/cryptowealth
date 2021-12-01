from fastapi import APIRouter

from apis.version1 import route_accounts
from apis.version1 import route_customers
from apis.version1 import route_general_pages
from apis.version1 import route_login

api_router = APIRouter()
api_router.include_router(
    route_general_pages.general_pages_router, prefix="", tags=["general_pages"]
)
api_router.include_router(
    route_customers.router, prefix="/customers", tags=["customers"]
)
api_router.include_router(
    route_accounts.router, prefix="/normal_accounts", tags=["accounts"]
)
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
