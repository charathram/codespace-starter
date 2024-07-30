from sqlalchemy.orm import Session
from app.db.models.plan import Plan
from app.schemas.plan import PlanCreate, PlanUpdate


def get(db: Session, id: int) -> Plan:
    return db.get(Plan, id)

def get_multi(db: Session) -> list[Plan]:
    return db.query(Plan).all()

def create(db: Session, *, obj_in: PlanCreate) -> Plan:
    db_obj = Plan(
        title=obj_in.title,
        description=obj_in.description,
        renewal_period=obj_in.renewal_period
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update(db: Session, *, db_obj: Plan, obj_in: PlanUpdate) -> Plan:
    update_data = obj_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def remove(db: Session, *, id: int) -> Plan:
    db_obj = db.get(Plan, id)
    db.delete(db_obj)
    db.commit()
    return db_obj
