from sqlalchemy import CheckConstraint, Column, Float, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Plan(Base):
    __tablename__ = "plans"  # Ensure the table name is "plans"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, unique=True, nullable=False)
    description = Column(String, nullable=False)
    renewal_period = Column(Integer, nullable=False)
    tier = Column(Integer, nullable=False)
    discount = Column(Float, nullable=False)

    __table_args__ = (
        CheckConstraint("renewal_period >= 1", name="renewal_period_check"),
    )
