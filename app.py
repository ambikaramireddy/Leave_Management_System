
import streamlit as st
import json
import pandas as pd
from datetime import date

# ---------------- FILE PATHS ----------------
EMP_FILE = "LMSDATA.json"
LEAVE_FILE = "leaves.json"

# ---------------- LOAD EMPLOYEE DATA ----------------
with open(EMP_FILE, "r") as file:
    LMS_DATA = json.load(file)

# ---------------- LEAVE FILE FUNCTIONS ----------------
def load_leaves():
    try:
        with open(LEAVE_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_leaves(data):
    with open(LEAVE_FILE, "w") as file:
        json.dump(data, file, indent=4)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Leave Management System", layout="wide")
st.title(" Leave Management System")

# ---------------- SESSION STATE ----------------
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

if "employee_logged_in" not in st.session_state:
    st.session_state.employee_logged_in = False

if "current_user" not in st.session_state:
    st.session_state.current_user = None

# ---------------- SIDEBAR ----------------
menu = st.sidebar.selectbox("Login As", [
    "Employee Login",
    "Manager Login"
])

# =================================================
# EMPLOYEE LOGIN
# =================================================
if menu == "Employee Login":

    st.header("Employee Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        user = next(
            (u for u in LMS_DATA if u["email"] == email and u["password"] == password),
            None
        )

        if user:
            st.session_state.employee_logged_in = True
            st.session_state.current_user = user
            st.success(" Employee Login Successful")
        else:
            st.error(" Invalid Credentials")

# =================================================
# ADMIN LOGIN
# =================================================
elif menu == "Manager Login":

    st.header("Manager Login")

    adminid = st.text_input("Manager Id")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if adminid == "222P1A3239" and password == "Ambika@69":
            st.session_state.admin_logged_in = True
            st.success(" Manager Login Successful")
        else:
            st.error(" Invalid Credentials")

# =================================================
# EMPLOYEE DASHBOARD
# =================================================
if st.session_state.employee_logged_in:

    user = st.session_state.current_user
    st.sidebar.success(f"Employee: {user['name']}")

    option = st.selectbox("Menu", [
        "Available Leaves",
        "Apply Leave",
        "My Leaves"
    ])

    # ---------------- AVAILABLE LEAVES ----------------
    if option == "Available Leaves":

        st.subheader(" Available Leaves")

        leave_balance = {
            "Casual Leave": 12,
            "Sick Leave": 10,
            "Earned Leave": 15
        }

        st.table(pd.DataFrame([
            {"Leave Type": k, "Available": v}
            for k, v in leave_balance.items()
        ]))

    # ---------------- APPLY LEAVE ----------------
    elif option == "Apply Leave":

        st.subheader(" Apply Leave")

        leave_type = st.selectbox("Leave Type", [
            "Casual Leave", "Sick Leave", "Earned Leave"
        ])

        start_date = st.date_input("Start Date", date.today())
        end_date = st.date_input("End Date", date.today())
        reason = st.text_area("Reason")

        if st.button("Submit Leave"):

            leaves = load_leaves()

            new_leave = {
                "id": len(leaves) + 1,
                "name": user["name"],
                "email": user["email"],
                "leave_type": leave_type,
                "start_date": str(start_date),
                "end_date": str(end_date),
                "reason": reason,
                "status": "Pending"
            }

            leaves.append(new_leave)
            save_leaves(leaves)

            st.success(" Leave Applied Successfully")

    # ---------------- MY LEAVES ----------------
    elif option == "My Leaves":

        st.subheader(" My Leaves")

        leaves = load_leaves()

        my_leaves = [
            l for l in leaves
            if l["email"] == user["email"]
        ]

        if my_leaves:
            st.dataframe(pd.DataFrame(my_leaves), use_container_width=True)
        else:
            st.info("No leaves applied yet.")

# =================================================
# ADMIN DASHBOARD (TABLE VIEW + ACTION)
# =================================================
if st.session_state.admin_logged_in:

    st.sidebar.success("Manager Logged In")
    st.subheader("🛠 Admin Dashboard")

    leaves = load_leaves()

    if leaves:

        df = pd.DataFrame(leaves)

        #  SHOW TABLE
        st.markdown("###  All Leave Requests")
        st.dataframe(df, use_container_width=True)

        #  FILTER
        status_filter = st.selectbox(
            "Filter by Status",
            ["All", "Pending", "Approved", "Rejected"]
        )

        if status_filter != "All":
            filtered_df = df[df["status"] == status_filter]
            st.dataframe(filtered_df, use_container_width=True)

        # ACTION
        st.markdown("### ✏️ Update Leave Status")

        pending_ids = [
            leave["id"] for leave in leaves if leave["status"] == "Pending"
        ]

        if pending_ids:

            selected_id = st.selectbox("Select Leave ID", pending_ids)
            action = st.radio("Action", ["Approve", "Reject"])

            if st.button("Submit"):

                for leave in leaves:
                    if leave["id"] == selected_id:
                        leave["status"] = "Approved" if action == "Approve" else "Rejected"

                save_leaves(leaves)

                st.success(f" Leave {selected_id} updated")
                st.rerun()
        else:
            st.info("No pending leaves to update")

    else:
        st.info("No leave requests found")

# =================================================
# LOGOUT
# =================================================
if st.sidebar.button("Logout"):

    st.session_state.admin_logged_in = False
    st.session_state.employee_logged_in = False
    st.session_state.current_user = None

    st.rerun()