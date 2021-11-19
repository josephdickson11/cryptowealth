from sqlalchemy import Column, Integer, String, Boolean, DATE, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Customer(Base):
    id = Column(Integer, primary_key= True, index=True)
    firstname = Column(String, nullable=True)
    lastname = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_KYC = Column(Boolean, default=False)
    accounts = relationship("Accounts", back_populates="owner")