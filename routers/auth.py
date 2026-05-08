
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(data: schemas.LoginSchema, db: Session = Depends(get_db)):
    user = crud.login(db, data.email, data.password)

    if not user:
        return {"error": "Invalid user"}

    return {
        "user_id": user.id,
        "role": user.role
    }