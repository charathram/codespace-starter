from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.crud import subscription as crud_subscription
from app.schemas import subscription as schemas
from app.db.models import subscription as models
from app import dependencies as deps
from app.db.models.user import User

router = APIRouter()


@router.get("/", response_model=List[schemas.Subscription])
def get_subscriptions(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> List[schemas.Subscription]:
    return crud_subscription.get_subscriptions(db=db, user_id=current_user.id)


@router.post("/", response_model=schemas.Subscription)
def create_subscription(
    *,
    db: Session = Depends(deps.get_db),
    subscription_in: schemas.SubscriptionCreate,
    current_user: User = Depends(deps.get_current_user),
) -> models.Subscription:
    try:
        return crud_subscription.create_subscription(db=db, subscription=subscription_in)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.get("/{id}", response_model=schemas.Subscription)
def get_subscription(
    *,
    db: Session = Depends(get_db),
    id: int,
):
    subscription = crud_subscription.get_subscription(db=db, subscription_id=id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription


@router.put("/{subscription_id}", response_model=schemas.Subscription)
def update_subscription(
    *,
    db: Session = Depends(deps.get_db),
    subscription_id: int,
    subscription_in: schemas.SubscriptionUpdate,
    current_user: User = Depends(deps.get_current_user),
) -> models.Subscription:
    subscription = crud_subscription.get_subscription(db=db, subscription_id=subscription_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")

    updated_subscription = crud_subscription.update_subscription(
        db=db, subscription_id=subscription.id, subscription_in=subscription_in
    )
    if not updated_subscription:
        raise HTTPException(status_code=400, detail="Failed to update subscription")
    return updated_subscription


@router.delete("/{subscription_id}", response_model=schemas.Subscription)
def delete_subscription(
    *,
    db: Session = Depends(deps.get_db),
    subscription_id: int,
    current_user: User = Depends(deps.get_current_user),
) -> models.Subscription:
    subscription = crud_subscription.get_subscription(
        db=db, subscription_id=subscription_id
    )
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return crud_subscription.delete_subscription(db=db, subscription_id=subscription_id)
