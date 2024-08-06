from sqlalchemy.orm import Session
from app.db.models.magazine import Magazine
from app.schemas.magazine import MagazineCreate, MagazineUpdate


def get_magazine(db: Session, magazine_id: int) -> Magazine:
    return db.query(Magazine).filter(Magazine.id == magazine_id).first()


def get_magazines(db: Session) -> list[Magazine]:
    return db.query(Magazine).all()


def create_magazine(db: Session, magazine_in: MagazineCreate) -> Magazine:
    db_obj = Magazine(**magazine_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_magazine(
    db: Session, magazine_id: int, magazine_in: MagazineUpdate
) -> Magazine:
    db_obj = get_magazine(db, magazine_id)
    if db_obj:
        for key, value in magazine_in.dict(exclude_unset=True).items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj


def delete_magazine(db: Session, magazine_id: int) -> Magazine:
    db_obj = get_magazine(db, magazine_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
