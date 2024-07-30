from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.magazine import Magazine, MagazineCreate, MagazineUpdate
from app.crud import magazine as crud_magazine


router = APIRouter()


@router.get("/", response_model=List[Magazine])
def read_magazines(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    magazines = crud_magazine.get_magazines(db, skip=skip, limit=limit)
    return magazines


@router.post("/", response_model=Magazine)
def create_magazine(magazine: MagazineCreate, db: Session = Depends(get_db)):
    return crud_magazine.create_magazine(db=db, magazine=magazine)


@router.get("/{magazine_id}", response_model=Magazine)
def retrieve_magazine(
    *,
    db: Session = Depends(get_db),
    magazine_id: int
):
    magazine = crud_magazine.get_magazine(db=db, magazine_id=magazine_id)
    if not magazine:
        raise HTTPException(status_code=404, detail="Magazine not found")
    return magazine


@router.put("/{magazine_id}", response_model=Magazine)
def update_magazine(
    magazine_id: int, magazine: MagazineUpdate, db: Session = Depends(get_db)
):
    return crud_magazine.update_magazine(
        db=db, magazine_id=magazine_id, magazine=magazine
    )


@router.delete("/{magazine_id}", response_model=Magazine)
def delete_magazine(magazine_id: int, db: Session = Depends(get_db)):
    return crud_magazine.delete_magazine(db=db, magazine_id=magazine_id)
