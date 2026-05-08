
from fastapi import FastAPI
from database import Base, engine
from routers import auth, employee, admin

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/", tags=["Home"])
def home():
    return {"message": "Leave Management System API"}

app.include_router(auth.router)
app.include_router(employee.router)
app.include_router(admin.router)