from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from db.base_class import Base


class Customer(Base):
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=True)
    lastname = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_KYC = Column(Boolean, default=False)
    total_account = Column(Integer, nullable=True)
    referral_id = Column(String, nullable=True, unique=True)
    referred_by = Column(String, nullable=True)
    accounts = relationship("Normal_accounts", back_populates="customer")
