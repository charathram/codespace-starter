from pydantic import BaseModel, ConfigDict, Field


class MagazineBase(BaseModel):
    name: str
    description: str
    base_price: float = Field(..., gt=0)


class MagazineCreate(MagazineBase):
    pass


class MagazineUpdate(MagazineBase):
    pass


class Magazine(MagazineBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
