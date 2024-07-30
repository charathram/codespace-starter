from sqlalchemy.orm import Session
from app.db.models.magazine import Magazine
from app.schemas.magazine import MagazineCreate, MagazineUpdate


def get_magazine(db: Session, magazine_id: int) -> Magazine:
    return db.query(Magazine).filter(Magazine.id == magazine_id).first()


def get_magazines(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Magazine).offset(skip).limit(limit).all()


def create_magazine(db: Session, magazine: MagazineCreate):
    db_magazine = Magazine(**magazine.model_dump())
    db.add(db_magazine)
    db.commit()
    db.refresh(db_magazine)
    return db_magazine


def update_magazine(db: Session, magazine_id: int, magazine: MagazineUpdate):
    db_magazine = db.query(Magazine).filter(Magazine.id == magazine_id).first()
    if db_magazine:
        for key, value in magazine.model_dump(exclude_unset=True).items():
            setattr(db_magazine, key, value)
        db.commit()
        db.refresh(db_magazine)
    return db_magazine


def delete_magazine(db: Session, magazine_id: int):
    db_magazine = db.query(Magazine).filter(Magazine.id == magazine_id).first()
    if db_magazine:
        db.delete(db_magazine)
        db.commit()
    return db_magazine
