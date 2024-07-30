from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import plan as crud_plan
from app.schemas.plan import Plan, PlanCreate, PlanUpdate
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=Plan)
def create_plan(
    *,
    db: Session = Depends(get_db),
    plan_in: PlanCreate,
):
    return crud_plan.create(db=db, obj_in=plan_in)

@router.get("/{id}", response_model=Plan)
def retrieve_plan(
    *,
    db: Session = Depends(get_db),
    id: int,
):
    plan = crud_plan.get(db=db, id=id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan

@router.get("/", response_model=list[Plan])
def get_plans(
    db: Session = Depends(get_db),
):
    plans = crud_plan.get_multi(db=db)
    return plans

@router.put("/{id}", response_model=Plan)
def update_plan(
    *,
    db: Session = Depends(get_db),
    id: int,
    plan_in: PlanUpdate,
):
    plan = crud_plan.get(db=db, id=id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    plan = crud_plan.update(db=db, db_obj=plan, obj_in=plan_in)
    return plan

@router.delete("/{id}", response_model=Plan)
def delete_plan(
    *,
    db: Session = Depends(get_db),
    id: int,
):
    plan = crud_plan.get(db=db, id=id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")
    plan = crud_plan.remove(db=db, id=id)
    return plan
