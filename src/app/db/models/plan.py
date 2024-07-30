from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Plan(Base):
    __tablename__ = "plans"  # Ensure the table name is "plans"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    renewal_period = Column(Integer, nullable=False)

    subscriptions = relationship("Subscription", back_populates="plan")
