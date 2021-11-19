from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey,
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null


from db.base_class import Base

class Normal_accounts(Base):
    id = Column(Integer, primary_key=True, index=True)
    asset_1 = Column(String, nullable=True)
    asset_2 = Column(String, nullable=True)
    asset_3 = Column(String, nullable=True)
    asset_4 = Column(String, nullable=True)
    asset_5 = Column(String, nullable=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="accounts")