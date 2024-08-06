from sqlalchemy.orm import Session
from app.db.models.plan import Plan
from app.schemas.plan import PlanCreate, PlanUpdate


def get_plan(db: Session, plan_id: int) -> Plan:
    return db.query(Plan).filter(Plan.id == plan_id).first()


def get_plans(db: Session) -> list[Plan]:
    return db.query(Plan).all()


def create_plan(db: Session, plan_in: PlanCreate) -> Plan:
    db_obj = Plan(**plan_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_plan(db: Session, plan_id: int, plan_in: PlanUpdate) -> Plan:
    db_obj = get_plan(db, plan_id)
    if db_obj:
        for key, value in plan_in.dict(exclude_unset=True).items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj


def delete_plan(db: Session, plan_id: int) -> Plan:
    db_obj = get_plan(db, plan_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
