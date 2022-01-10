from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from db.base_class import Base


class Investor_profile(Base):
    id = Column(Integer, primary_key=True, index=True)
    risk_level = Column(String, nullable=True)
    invest_purpose = Column(String, nullable=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="investor_profile")
