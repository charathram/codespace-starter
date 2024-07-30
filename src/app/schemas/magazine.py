from pydantic import BaseModel, ConfigDict
from typing import Optional


class MagazineBase(BaseModel):
    name: str
    description: str
    base_price: float
    discount_quarterly: Optional[float] = None
    discount_half_yearly: Optional[float] = None
    discount_annual: Optional[float] = None


class MagazineCreate(MagazineBase):
    pass


class MagazineUpdate(MagazineBase):
    pass


class Magazine(MagazineBase):
    id: int
    model_config = ConfigDict(from_attributes=True)