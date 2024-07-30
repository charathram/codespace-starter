from pydantic import BaseModel, Field, ConfigDict
from datetime import date

class SubscriptionBase(BaseModel):
    user_id: int
    magazine_id: int
    plan_id: int
    price: float
    next_renewal_date: date

class SubscriptionCreate(SubscriptionBase):
    pass

class SubscriptionUpdate(SubscriptionBase):
    pass

class SubscriptionInDBBase(SubscriptionBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class Subscription(SubscriptionInDBBase):
    pass

class SubscriptionInDB(SubscriptionInDBBase):
    pass
