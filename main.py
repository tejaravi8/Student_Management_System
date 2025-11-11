from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import sqlite3

# ------------------ APP SETUP ------------------
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="supersecretkey123")

templates = Jinja2Templates(directory="templates")

# ------------------ DATABASE SETUP ------------------
db = sqlite3.connect("database.db", check_same_thread=False)
cursor = db.cursor()

# Create tables if they don't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    course TEXT,
    role TEXT DEFAULT 'user'
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT,
    created_by TEXT
)
""")
db.commit()

# Ensure admin account exists
cursor.execute("SELECT * FROM users WHERE email='admin@portal.com'")
if not cursor.fetchone():
    cursor.execute(
        "INSERT INTO users (name, email, password, course, role) VALUES (?, ?, ?, ?, ?)",
        ("Admin", "admin@portal.com", "admin123", "Management", "admin")
    )
    db.commit()


# ------------------ HOME PAGE ------------------
@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    user = request.session.get("user")
    role = request.session.get("role")
    return templates.TemplateResponse("home.html", {"request": request, "user": user, "role": role})


# ------------------ SIGNUP ------------------
@app.get("/signup", response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup")
def signup_user(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    course: str = Form(...)
):
    try:
        cursor.execute(
            "INSERT INTO users (name, email, password, course, role) VALUES (?, ?, ?, ?, ?)",
            (name, email, password, course, "user")
        )
        db.commit()
        return RedirectResponse("/login", status_code=303)
    except sqlite3.IntegrityError:
        return templates.TemplateResponse(
            "signup.html",
            {
                "request": request,
                "error": "⚠️ This email is already registered.",
                "name": name,
                "email": email,
                "course": course
            }
        )


# ------------------ LOGIN ------------------
@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login_user(
    request: Request,
    email: str = Form(...),
    password: str = Form(...)
):
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()

    if not user:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "❌ No account found with this email.", "email": email}
        )

    if user[3] != password:  # password column
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "⚠️ Wrong password. Please try again.", "email": email}
        )

    # Save session
    request.session["user"] = user[1]  # name
    request.session["email"] = user[2] # email
    request.session["role"] = user[5]  # role

    if user[5] == "admin":
        return RedirectResponse("/admin/dashboard", status_code=303)
    else:
        return RedirectResponse("/user/profile", status_code=303)


# ------------------ LOGOUT ------------------
@app.get("/logout")
def logout_user(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)


# ------------------ ADMIN DASHBOARD ------------------
@app.get("/admin/dashboard", response_class=HTMLResponse)
def admin_dashboard(request: Request):
    user = request.session.get("user")
    role = request.session.get("role")

    if not user or role != "admin":
        return RedirectResponse("/login", status_code=303)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    return templates.TemplateResponse(
        "admin_dashboard.html",
        {"request": request, "user": user, "students": students}
    )


# ------------------ ADMIN CRUD ------------------
@app.get("/admin/add-student", response_class=HTMLResponse)
def add_student_page(request: Request):
    user = request.session.get("user")
    role = request.session.get("role")

    if not user or role != "admin":
        return RedirectResponse("/login", status_code=303)

    return templates.TemplateResponse("add_student.html", {"request": request, "user": user})

@app.post("/admin/add-student")
def add_student(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    course: str = Form(...)
):
    user = request.session.get("user")
    role = request.session.get("role")

    if not user or role != "admin":
        return RedirectResponse("/login", status_code=303)

    cursor.execute(
        "INSERT INTO students (name, age, course, created_by) VALUES (?, ?, ?, ?)",
        (name, age, course, user)
    )
    db.commit()
    return RedirectResponse("/admin/dashboard", status_code=303)

@app.get("/admin/delete-student/{student_id}")
def delete_student(request: Request, student_id: int):
    user = request.session.get("user")
    role = request.session.get("role")

    if not user or role != "admin":
        return RedirectResponse("/login", status_code=303)

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    db.commit()
    return RedirectResponse("/admin/dashboard", status_code=303)

@app.get("/admin/edit-student/{student_id}", response_class=HTMLResponse)
def edit_student_page(request: Request, student_id: int):
    user = request.session.get("user")
    role = request.session.get("role")

    if not user or role != "admin":
        return RedirectResponse("/login", status_code=303)

    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    student = cursor.fetchone()
    return templates.TemplateResponse("edit_student.html", {"request": request, "user": user, "student": student})

@app.post("/admin/edit-student/{student_id}")
def update_student(
    request: Request,
    student_id: int,
    name: str = Form(...),
    age: int = Form(...),
    course: str = Form(...)
):
    user = request.session.get("user")
    role = request.session.get("role")

    if not user or role != "admin":
        return RedirectResponse("/login", status_code=303)

    cursor.execute("UPDATE students SET name=?, age=?, course=? WHERE id=?", (name, age, course, student_id))
    db.commit()
    return RedirectResponse("/admin/dashboard", status_code=303)


# ------------------ USER PROFILE ------------------
@app.get("/user/profile", response_class=HTMLResponse)
def user_profile(request: Request):
    email = request.session.get("email")
    if not email:
        return RedirectResponse("/login", status_code=303)

    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user_data = cursor.fetchone()

    return templates.TemplateResponse(
        "user_profile.html",
        {"request": request, "user": user_data}
    )

@app.post("/user/profile/update")
def update_profile(
    request: Request,
    name: str = Form(...),
    course: str = Form(...),
    password: str = Form(...)
):
    email = request.session.get("email")
    if not email:
        return RedirectResponse("/login", status_code=303)

    cursor.execute("UPDATE users SET name=?, course=?, password=? WHERE email=?", (name, course, password, email))
    db.commit()
    return RedirectResponse("/user/profile", status_code=303)
