from datetime import date
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null


from db.base_class import Base

class Normal_accounts(Base):
    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(Integer, nullable=False)
    wallet_id = Column(Integer, primary_key=True)
    date_created = Column(Date)
    wallet_balance = Column(Integer)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="accounts")