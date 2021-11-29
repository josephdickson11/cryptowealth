from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null


from db.base_class import Base

class Normal_accounts(Base):
    id = Column(Integer, primary_key=True, index=True)
    wallet_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="accounts")