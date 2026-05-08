
import hashlib
from sqlalchemy.orm import Session
from datetime import date
import models

#  HASH PASSWORD
def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

#  VERIFY PASSWORD
def verify_password(input_password: str, stored_password: str):
    return hash_password(input_password) == stored_password


# =========================
#  AUTH
# =========================
def login(db: Session, email: str, password: str):
    user = db.query(models.Employee).filter(models.Employee.email == email).first()

    if not user:
        return {"error": "User not found"}

    if not verify_password(password, user.password):
        return {"error": "Invalid password"}

    return user


# =========================
# 👤 EMPLOYEE
# =========================
def create_employee(db: Session, emp):
    hashed_pwd = hash_password(emp.password)

    new_emp = models.Employee(
        emp_code=emp.emp_code,
        name=emp.name,
        email=emp.email,
        password=hashed_pwd,
        role=emp.role,
        department=emp.department
    )

    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp


def get_employee_by_id(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()


# =========================
#  APPLY LEAVE
# =========================
def apply_leave(db: Session, emp_id: int, leave):

    #  Check employee exists
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        return {"error": "Employee not found"}

    #  Date validation
    if leave.start_date > leave.end_date:
        return {"error": "Start date cannot be after end date"}

    #  Past date check
    if leave.start_date < date.today():
        return {"error": "Cannot apply for past dates"}

    #  Overlap check
    existing = db.query(models.Leave).filter(
        models.Leave.employee_id == emp_id,
        models.Leave.start_date <= leave.end_date,
        models.Leave.end_date >= leave.start_date
    ).first()

    if existing:
        return {"error": "Leave overlap detected"}

    #  Create leave
    new_leave = models.Leave(
        employee_id=emp_id,
        leave_type=leave.leave_type,
        start_date=leave.start_date,
        end_date=leave.end_date,
        reason=leave.reason,
        status="Pending"
    )

    db.add(new_leave)
    db.commit()
    db.refresh(new_leave)

    return new_leave


# =========================
#  GET LEAVES
# =========================
def get_my_leaves(db: Session, emp_id: int):
    return db.query(models.Leave).filter(models.Leave.employee_id == emp_id).all()


# =========================
#  UPDATE LEAVE
# =========================
def update_leave(db: Session, leave_id: int, data):
    leave = db.query(models.Leave).filter(models.Leave.id == leave_id).first()

    if not leave:
        return {"error": "Leave not found"}

    #  Only pending allowed
    if leave.status != "Pending":
        return {"error": "Only pending leave can be updated"}

    #  Date validation
    if data.start_date > data.end_date:
        return {"error": "Invalid date range"}

    if data.start_date < date.today():
        return {"error": "Cannot update with past dates"}

    #  Update fields
    leave.leave_type = data.leave_type
    leave.start_date = data.start_date
    leave.end_date = data.end_date
    leave.reason = data.reason

    db.commit()
    db.refresh(leave)

    return leave


# =========================
#  DELETE LEAVE
# =========================
def delete_leave(db: Session, leave_id: int):
    leave = db.query(models.Leave).filter(models.Leave.id == leave_id).first()

    if not leave:
        return {"error": "Leave not found"}

    if leave.status != "Pending":
        return {"error": "Only pending leave can be deleted"}

    db.delete(leave)
    db.commit()

    return {"message": "Deleted successfully"}


# =========================
#  ADMIN ACTIONS
# =========================
def approve_leave(db: Session, leave_id: int):
    leave = db.query(models.Leave).filter(models.Leave.id == leave_id).first()

    if not leave:
        return {"error": "Leave not found"}

    if leave.status != "Pending":
        return {"error": "Already processed"}

    leave.status = "Approved"
    db.commit()
    db.refresh(leave)

    return leave


def reject_leave(db: Session, leave_id: int):
    leave = db.query(models.Leave).filter(models.Leave.id == leave_id).first()

    if not leave:
        return {"error": "Leave not found"}

    if leave.status != "Pending":
        return {"error": "Already processed"}

    leave.status = "Rejected"
    db.commit()
    db.refresh(leave)

    return leave