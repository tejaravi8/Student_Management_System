# 🎓 Student Management Portal (FastAPI + SQLite)

A simple **Student Management Web Application** built using **FastAPI**, **Jinja2 Templates**, and **SQLite** database.  
It supports:
- User Signup/Login
- Admin Dashboard
- Add/Edit/Delete Students
- User Profile Management

---

## 🚀 Features

| Role | Permissions |
|------|--------------|
| **Admin** | Add, Edit, Delete Students, View All Students |
| **User** | View & Update Own Profile |
| **Guest** | Register or Login |

---

## 🧰 Tech Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
- **Frontend:** HTML, CSS, [Bootstrap 5](https://getbootstrap.com/)
- **Database:** SQLite (file-based, no server needed)
- **Templating Engine:** Jinja2
- **Server:** Uvicorn

---

## 📁 Project Structure
FastAPI_Project/
│
├── main.py
├── requirements.txt
├── README.md
└── templates/
├── home.html
├── signup.html
├── login.html
├── user_profile.html
├── admin_dashboard.html
├── add_student.html
└── edit_student.html
