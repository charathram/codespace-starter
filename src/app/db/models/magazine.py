from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Magazine(Base):
    __tablename__ = "magazines"  # Ensure the table name is "magazines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    base_price = Column(Float, nullable=False)
    discount_quarterly = Column(Float, nullable=False)
    discount_half_yearly = Column(Float, nullable=False)
    discount_annual = Column(Float, nullable=False)

    subscriptions = relationship("Subscription", back_populates="magazine")
