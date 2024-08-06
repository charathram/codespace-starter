from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.db.models import magazine as models
from app.schemas.magazine import Magazine, MagazineCreate, MagazineUpdate
from app.crud import magazine as crud_magazine
from app import dependencies as deps

router = APIRouter()


@router.get("/", response_model=List[Magazine])
def get_magazines(
    db: Session = Depends(deps.get_db),
) -> List[Magazine]:
    return crud.magazine.get_magazines(db)


@router.post("/", response_model=Magazine)
def create_magazine(
    *,
    db: Session = Depends(deps.get_db),
    magazine_in: MagazineCreate,
) -> models.Magazine:
    return crud.magazine.create_magazine(db=db, magazine_in=magazine_in)


@router.get("/{magazine_id}", response_model=Magazine)
def get_magazine(*, db: Session = Depends(deps.get_db), magazine_id: int):
    magazine = crud_magazine.get_magazine(db=db, magazine_id=magazine_id)
    if not magazine:
        raise HTTPException(status_code=404, detail="Magazine not found")
    return magazine


@router.put("/{magazine_id}", response_model=Magazine)
def update_magazine(
    *,
    db: Session = Depends(deps.get_db),
    magazine_id: int,
    magazine_in: MagazineUpdate,
) -> models.Magazine:
    magazine = crud.magazine.get_magazine(db=db, magazine_id=magazine_id)
    if not magazine:
        raise HTTPException(status_code=404, detail="Magazine not found")
    return crud.magazine.update_magazine(
        db=db, magazine_id=magazine_id, magazine_in=magazine_in
    )


@router.delete("/{magazine_id}", response_model=Magazine)
def delete_magazine(
    *,
    db: Session = Depends(deps.get_db),
    magazine_id: int,
) -> models.Magazine:
    magazine = crud.magazine.get_magazine(db=db, magazine_id=magazine_id)
    if not magazine:
        raise HTTPException(status_code=404, detail="Magazine not found")
    return crud.magazine.delete_magazine(db=db, magazine_id=magazine_id)
