from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import validates
from app.db.base_class import Base


class Magazine(Base):
    __tablename__ = "magazines"  # Ensure the table name is "magazines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True, nullable=False)
    description = Column(String, nullable=False)
    base_price = Column(Float, nullable=False)

    @validates("base_price")
    def validate_base_price(self, key, value):
        assert value > 0, "Base price must be greater than zero"
        return value
