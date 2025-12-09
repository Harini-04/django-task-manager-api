# 📝 Task Manager Backend API

A production-style backend API built using Django REST Framework with JWT authentication.  
This project supports secure user authentication and user-scoped task management.

---

## 🚀 Features

- User authentication using JWT
- CRUD operations for tasks
- Each task is owned by a user
- Users can see and modify only their own tasks
- Filtering, searching, ordering, and pagination
- PostgreSQL as the primary database

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)

---

## 🔐 Authentication

This project uses **JWT (JSON Web Token)** authentication.

- Obtain token: `POST /api/token/`
- Use the access token in requests:
- All task APIs require authentication.

---

## 📌 API Endpoints

### Authentication
- `POST /api/token/` – Get access & refresh token
- `POST /api/token/refresh/` – Refresh access token

### Tasks
- `GET /api/tasks/` – List user tasks
- `POST /api/tasks/` – Create a task
- `GET /api/tasks/{id}/` – Retrieve a task
- `PUT /api/tasks/{id}/` – Update a task
- `PATCH /api/tasks/{id}/` – Partial update
- `DELETE /api/tasks/{id}/` – Delete a task

---

## 🔒 Permission Logic

- Only authenticated users can access APIs
- Each task is linked to an owner
- Users can view, update, or delete **only their own tasks**

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
- git clone <repo-url>
- cd task-manager-backend

### 2️⃣ Create and activate virtual environment
- python -m venv venv
- venv\Scripts\activate

### 3️⃣ Install dependencies
- pip install -r requirements.txt

### 4️⃣ Create .env file

### 5️⃣ Run migrations
- python manage.py makemigrations
- python manage.py migrate

### 6️⃣ Start the server
- python manage.py runserver
