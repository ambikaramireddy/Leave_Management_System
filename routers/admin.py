
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/all-leaves")
def all_leaves(db: Session = Depends(get_db)):
    return crud.get_all_leaves(db)


@router.put("/approve/{leave_id}")
def approve(leave_id: int, db: Session = Depends(get_db)):
    return crud.approve_leave(db, leave_id)


@router.put("/reject/{leave_id}")
def reject(leave_id: int, db: Session = Depends(get_db)):
    return crud.reject_leave(db, leave_id)