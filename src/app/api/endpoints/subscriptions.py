from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import subscription as crud_subscription
from app.schemas.subscription import Subscription, SubscriptionCreate, SubscriptionUpdate
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=Subscription)
def create_subscription(
    *,
    db: Session = Depends(get_db),
    subscription_in: SubscriptionCreate,
):
    return crud_subscription.create(db=db, obj_in=subscription_in)

@router.get("/{id}", response_model=Subscription)
def retrieve_subscription(
    *,
    db: Session = Depends(get_db),
    id: int,
):
    subscription = crud_subscription.get(db=db, id=id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription

@router.get("/", response_model=list[Subscription])
def get_subscriptions(
    db: Session = Depends(get_db),
):
    subscriptions = crud_subscription.get_multi(db=db)
    return subscriptions

@router.put("/{id}", response_model=Subscription)
def update_subscription(
    *,
    db: Session = Depends(get_db),
    id: int,
    subscription_in: SubscriptionUpdate,
):
    subscription = crud_subscription.get(db=db, id=id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    subscription = crud_subscription.update(db=db, db_obj=subscription, obj_in=subscription_in)
    return subscription


@router.delete("/{subscription_id}", response_model=Subscription)
def delete_subscription(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = crud_subscription.get(db, subscription_id)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")

    db_subscription.is_active = False
    db.commit()
    db.refresh(db_subscription)
    return db_subscription