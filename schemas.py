
from pydantic import BaseModel
from datetime import date
from typing import Optional

# =========================
#  AUTH
# =========================
class LoginSchema(BaseModel):
    email: str
    password: str


# =========================
#  EMPLOYEE
# =========================
class EmployeeCreate(BaseModel):
    emp_code: str
    name: str
    email: str
    password: str
    role: Optional[str] = "employee"
    department: str


class EmployeeResponse(BaseModel):
    id: int
    emp_code: str
    name: str
    email: str
    role: str
    department: str

    class Config:
        orm_mode = True


# =========================
#  LEAVE CREATE
# =========================
class LeaveCreate(BaseModel):
    leave_type: str
    start_date: date
    end_date: date
    reason: str


# =========================
#  LEAVE UPDATE
# =========================
class LeaveUpdate(BaseModel):
    leave_type: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    reason: Optional[str] = None


# =========================
#  LEAVE RESPONSE
# =========================
class LeaveResponse(BaseModel):
    id: int
    employee_id: int
    leave_type: str
    start_date: date
    end_date: date
    reason: str
    status: str

    class Config:
        from_attributes = True