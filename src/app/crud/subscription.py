from sqlalchemy.orm import Session
from app.db.models.magazine import Magazine
from app.db.models.plan import Plan
from app.db.models.subscription import Subscription
from app.schemas.subscription import SubscriptionCreate, SubscriptionUpdate


def get_subscription(db: Session, subscription_id: int) -> Subscription:
    return db.query(Subscription).filter(Subscription.id == subscription_id).first()


def get_subscriptions(db: Session, user_id: int) -> list[Subscription]:
    return (
        db.query(Subscription)
        .filter(Subscription.user_id == user_id, Subscription.is_active == True)
        .all()
    )


def create_subscription(
    db: Session, subscription: SubscriptionCreate
) -> Subscription:
    magazine = (
        db.query(Magazine).filter(Magazine.id == subscription.magazine_id).first()
    )
    plan = db.query(Plan).filter(Plan.id == subscription.plan_id).first()

    if not magazine or not plan:
        raise ValueError("Invalid magazine or plan ID")

    price = magazine.base_price * (1 - plan.discount)
    if price <= 0:
        raise ValueError("Price must be greater than zero")

    subscription = Subscription(
        user_id=subscription.user_id,
        magazine_id=subscription.magazine_id,
        plan_id=subscription.plan_id,
        price=price,
        renewal_date=subscription.renewal_date,
        is_active=True,
    )

    db.add(subscription)
    db.commit()
    db.refresh(subscription)
    return subscription


def update_subscription(
    db: Session, subscription_id: int, subscription_in: SubscriptionUpdate
) -> Subscription:
    # Get the existing subscription
    existing_subscription = (
        db.query(Subscription).filter(Subscription.id == subscription_id).first()
    )
    if not existing_subscription:
        return None

    magazine = (
        db.query(Magazine).filter(Magazine.id == subscription_in.magazine_id).first()
    )
    plan = db.query(Plan).filter(Plan.id == subscription_in.plan_id).first()
    # Deactivate the existing subscription
    existing_subscription.is_active = False
    db.add(existing_subscription)
    db.commit()
    db.refresh(existing_subscription)

    # Create a new subscription with the updated details
    new_subscription = Subscription(
        user_id=subscription_in.user_id,
        magazine_id=subscription_in.magazine_id,
        plan_id=subscription_in.plan_id,
        price=magazine.base_price * (1 - plan.discount),
        renewal_date=subscription_in.renewal_date,
        is_active=True,
    )
    db.add(new_subscription)
    db.commit()
    db.refresh(new_subscription)
    return new_subscription


def delete_subscription(db: Session, subscription_id: int) -> Subscription:
    db_obj = get_subscription(db, subscription_id)
    if db_obj:
        db_obj.is_active = False
        db.commit()
        db.refresh(db_obj)
    return db_obj
