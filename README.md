# 🎓 Student Management System (Django + TailwindCSS)

A clean and modern **Student Management Web Application** built using **Django**, **TailwindCSS**, and **SQLite**.  
This project includes full **CRUD operations**, a **dashboard with analytics**, and a **beautiful UI** powered by TailwindCSS.


## 🚀 Features

### 🔹 Core Features
- Add Student  
- Edit Student  
- Delete Student  
- View All Students (Table View)  
- TailwindCSS UI  
- Django ModelForms  

### 🔹 Dashboard Features
- Total Students Count  
- Average Age  
- Youngest & Oldest Student  
- Recently Added Students  
- Professional cards & tables  

### 🔹 UI/UX
- Responsive TailwindCSS design  
- Navbar with quick navigation  
- Alert messages (success/error)  
- Clean tables & forms  


## 📸 Screenshots
Add your screenshots here:

### Home

<img width="1920" height="1020" alt="Screenshot 2025-12-04 105821" src="https://github.com/user-attachments/assets/2b668b04-ea53-475d-b9ad-6c8dae486c70" />

### View Studenets

<img width="1920" height="1020" alt="Screenshot 2025-12-04 105848" src="https://github.com/user-attachments/assets/471424ee-c279-4fb0-9558-c80ba8fd000c" />

### Add Students

<img width="1920" height="1020" alt="Screenshot 2025-12-04 105859" src="https://github.com/user-attachments/assets/6927313e-6658-42e4-b71b-f6df4b16074b" />

### Dashboard

<img width="1920" height="1020" alt="Screenshot 2025-12-04 105909" src="https://github.com/user-attachments/assets/a5c2c963-164b-4554-8727-b9e9f65fa3ea" />

### Edit

<img width="1920" height="1020" alt="Screenshot 2025-12-04 110727" src="https://github.com/user-attachments/assets/fd981836-3987-4b96-acb1-44fb264c13f7" />


## 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Django 5** | Backend Framework |
| **SQLite** | Database |
| **TailwindCSS CDN** | Styling |
| **HTML / Django Templates** | Frontend |
| **ModelForms** | Form handling |



## 📂 Project Structure
```
myproject/
│── manage.py
│── myproject/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│
│── app/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── student_list.html
│ │ ├── add_student.html
│ │ ├── edit_student.html
│ │ └── dashboard.html
│
```


## ⚙️ Installation & Setup
```
1️⃣ Clone the repository

bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system

2️⃣ Create virtual environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate


macOS / Linux

source venv/bin/activate

3️⃣ Install dependencies
pip install django

4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run development server
python manage.py runserver

Open browser →
👉 http://127.0.0.1:8000/

```

## 📘 How It Works
⭐ Models

Student model for storing student data

Fields: name, age, email

⭐ Forms

Django ModelForm for easy field rendering

TailwindCSS styling via widgets

⭐ Views

Function-based views for CRUD

Dashboard powered by ORM queries

Avg, Min, Max

Latest entries

⭐ TailwindCSS

Included using CDN:
```
<script src="https://cdn.tailwindcss.com"></script>
```
## 📌 Future Enhancements

- Search functionality

- Pagination

- Sorting

- Profile photos (image upload)

- JWT Authentication

- REST API with Django REST Framework

- Deployment on Render / Railway


## 🤝 Contributing

Pull requests are welcome!
Feel free to open issues for enhancements.


## 💬 Author

Ravi Teja Botsa

GitHub: https://github.com/yourusername

Email: botsaraviteja@gmail.com
