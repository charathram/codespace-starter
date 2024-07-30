from pydantic import BaseModel, Field, ConfigDict, field_validator

class PlanBase(BaseModel):
    title: str
    description: str
    renewal_period: int

    @field_validator("renewal_period")
    def validate_renewal_period(cls, value):
        if value <= 0:
            raise ValueError("renewal_period must be greater than zero")
        return value

class PlanCreate(PlanBase):
    pass

class PlanUpdate(PlanBase):
    pass

class PlanInDBBase(PlanBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class Plan(PlanInDBBase):
    pass

class PlanInDB(PlanInDBBase):
    pass
