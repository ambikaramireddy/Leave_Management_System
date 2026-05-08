
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas

router = APIRouter(prefix="/employee", tags=["Employee"])

@router.post("/create")
def create_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, emp)


@router.post("/apply/{user_id}")
def apply_leave(user_id: int, leave: schemas.LeaveCreate, db: Session = Depends(get_db)):
    return crud.apply_leave(db, user_id, leave)


@router.get("/my-leaves/{user_id}")
def my_leaves(user_id: int, db: Session = Depends(get_db)):
    return crud.get_my_leaves(db, user_id)


@router.put("/{leave_id}")
def update_leave(leave_id: int, leave: schemas.LeaveCreate, db: Session = Depends(get_db)):
    return crud.update_leave(db, leave_id, leave)


@router.delete("/{leave_id}")
def delete_leave(leave_id: int, db: Session = Depends(get_db)):
    return crud.delete_leave(db, leave_id)