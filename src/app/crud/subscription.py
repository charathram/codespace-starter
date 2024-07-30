from sqlalchemy.orm import Session
from app.db.models.subscription import Subscription
from app.schemas.subscription import SubscriptionCreate, SubscriptionUpdate

def get(db: Session, id: int) -> Subscription:
    return db.query(Subscription).filter(Subscription.id == id).first()

def get_multi(db: Session) -> list[Subscription]:
    return db.query(Subscription).all()

def create(db: Session, *, obj_in: SubscriptionCreate) -> Subscription:
    db_obj = Subscription(
        user_id=obj_in.user_id,
        magazine_id=obj_in.magazine_id,
        plan_id=obj_in.plan_id,
        price=obj_in.price,
        next_renewal_date=obj_in.next_renewal_date,
        is_active=True,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update(db: Session, *, db_obj: Subscription, obj_in: SubscriptionUpdate) -> Subscription:
    update_data = obj_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def remove(db: Session, *, id: int) -> Subscription:
    db_obj = db.query(Subscription).get(id)
    db_obj.is_active = False
    db.commit()
    return db_obj
