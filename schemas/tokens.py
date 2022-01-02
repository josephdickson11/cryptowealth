from pydantic import BaseModel

from db.models.customer import Customer


class TokenData(BaseModel):
    access_token: str
    token_type: str
    Customer
