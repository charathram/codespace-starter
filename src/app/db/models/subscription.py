from sqlalchemy import Column, Integer, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship, validates
from app.db.base_class import Base

class Subscription(Base):
    __tablename__ = "subscriptions"  # Ensure the table name is "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    magazine_id = Column(Integer, ForeignKey('magazines.id'), nullable=False)
    plan_id = Column(Integer, ForeignKey('plans.id'), nullable=False)
    price = Column(Float, nullable=False)
    renewal_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="subscriptions")
    magazine = relationship("Magazine")
    plan = relationship("Plan")

    @validates('price')
    def validate_price(self, key, value):
        assert value > 0, "Price must be greater than zero"
        return value
