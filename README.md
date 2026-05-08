# 🌐 Live Demo

🔗 [Leave Management System](https://leavemanagementsystem-guf24gway87wqy8jpqbmu3.streamlit.app/)
# 📝 Leave Management System

## 📌 Project Overview

The **Leave Management System** is a web-based application developed using **FastAPI**, **Streamlit**, and **PostgreSQL** to simplify and automate employee leave management processes.

The system allows employees to apply for leave online, while admins can manage and approve/reject leave requests efficiently.

This project reduces manual paperwork and improves transparency between employees and administrators.

---

# 🎯 Objectives

- Automate leave request and approval workflow
- Maintain accurate employee leave records
- Reduce manual work and errors
- Provide secure authentication using JWT
- Improve leave tracking efficiency

---

# 👥 Users of the System

## 👨‍💼 Employee

- Register/Login securely
- Apply for leave
- View leave history
- Update/Delete leave requests

## 👨‍💻 Admin

- Approve or reject leave requests
- Manage employee leave records
- Monitor leave applications

---

# ⚙️ Features

- 🔐 JWT Authentication
- 📝 Employee Registration & Login
- 📅 Apply for Leave
- 📂 View Leave Records
- ✏️ Update Leave Requests
- ❌ Delete Leave Requests
- ✔️ Admin Leave Approval/Rejection
- 🗄️ PostgreSQL Database Integration
- 🌐 Streamlit Frontend UI
- ⚡ FastAPI Backend APIs

---

# 🏗️ System Modules

## 1️⃣ Authentication Module

- Secure Signup/Login
- Password Hashing using Passlib
- JWT Token Generation

## 2️⃣ Employee Module

- Apply leave requests
- View leave status/history
- Update or cancel leave

## 3️⃣ Admin Module

- Approve/Reject leave requests
- Manage leave records

---

# 🛠️ Technologies Used

## 🔹 Frontend
- Streamlit

## 🔹 Backend
- FastAPI
- Python

## 🔹 Database
- PostgreSQL

## 🔹 ORM
- SQLAlchemy

## 🔹 Authentication
- Python-Jose (JWT)
- Passlib (bcrypt)

---

# 📂 Project Structure

```bash
LMS/
│
├── main.py              # FastAPI Backend
├── app.py               # Streamlit Frontend
├── database.py          # Database Configuration
├── models.py            # Database Models
├── schemas.py           # Pydantic Schemas
├── crud.py              # Database Operations
├── auth.py              # JWT Authentication
├── dependencies.py      # DB Dependency
├── requirements.txt
└── README.md
# 🚀 How to Run the Project

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/leave-management-system.git
```

## 2️⃣ Navigate to Project Folder

```bash
cd leave-management-system
```

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment (Windows)

```bash
venv\Scripts\activate
```

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🐘 PostgreSQL Database Setup

Update your `database.py` file:

```python
DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/YOUR_DATABASE"
```

Replace:
- `YOUR_PASSWORD`
- `YOUR_DATABASE`

with your PostgreSQL credentials.

---

# ▶️ Run Backend Server

```bash
uvicorn main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

Swagger API Documentation:

```bash
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Frontend

Open another terminal and run:

```bash
streamlit run app.py
```

Frontend runs on:

```bash
http://localhost:8501
```


# 🔮 Future Enhancements

- 📧 Email Notifications
- 📊 Admin Dashboard Analytics
- 📱 Mobile Responsive UI
- 🔔 Real-Time Notifications
- 🧾 Leave Balance Tracking
- ☁️ Cloud Deployment

---

# 🤝 Contributing

Contributions are welcome!

Feel free to fork this repository and submit a pull request.

---

# 📄 License

This project is developed for educational purposes.

---

# 👨‍💻 Author

**Ambika Ramireddy**
