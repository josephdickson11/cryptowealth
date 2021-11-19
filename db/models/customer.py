from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class Customer(Base):
    id = Column(Integer, primary_key= True, index=True)
    firstname = Column(String, nullable=True)
    lastname = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_KYC = Column(Boolean, default=False)
    total_account = Column(Integer, nullable=True)
    accounts = relationship("Normal_accounts", back_populates="customer")