from fastapi import APIRouter, Depends, HTTPException
from app.db.session import get_db
from sqlalchemy.orm import Session
from typing import List
from app.schemas import plan as schemas
from app.db.models import plan as models
from app import dependencies as deps
from app.crud import plan as crud_plan

router = APIRouter()


@router.get("/", response_model=List[schemas.Plan])
def get_plans(
    db: Session = Depends(deps.get_db),
) -> List[schemas.Plan]:
    return crud_plan.get_plans(db)


@router.post("/", response_model=schemas.Plan)
def create_plan(
    *,
    db: Session = Depends(deps.get_db),
    plan_in: schemas.PlanCreate,
) -> models.Plan:
    return crud_plan.create_plan(db=db, plan_in=plan_in)


@router.get("/{id}", response_model=schemas.Plan)
def get_plan(
    *,
    db: Session = Depends(get_db),
    id: int,
):
    plan = crud_plan.get_plan(db=db, plan_id=id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan


@router.put("/{plan_id}", response_model=schemas.Plan)
def update_plan(
    *,
    db: Session = Depends(deps.get_db),
    plan_id: int,
    plan_in: schemas.PlanUpdate,
) -> models.Plan:
    plan = crud_plan.get_plan(db=db, plan_id=plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return crud_plan.update_plan(db=db, plan_id=plan_id, plan_in=plan_in)


@router.delete("/{plan_id}", response_model=schemas.Plan)
def delete_plan(
    *,
    db: Session = Depends(deps.get_db),
    plan_id: int,
) -> models.Plan:
    plan = crud_plan.get_plan(db=db, plan_id=plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return crud_plan.delete_plan(db=db, plan_id=plan_id)
