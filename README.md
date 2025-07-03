# DRF Blog with CKEditor 📝

A feature-rich blog backend built with **Django Rest Framework** and integrated **CKEditor** for rich text editing. This project is designed to showcase modular, scalable, and production-ready API development using Django.

![Python](https://img.shields.io/badge/python-3.10-blue)
![Django](https://img.shields.io/badge/django-4.2-green)
![DRF](https://img.shields.io/badge/DRF-3.14-orange)
![License](https://img.shields.io/github/license/YOUR_USERNAME/drf-blog-with-ckeditor)

---

## 🚀 Features

- ✅ Full CRUD for blog posts
- ✅ Rich text editing using `django-ckeditor`
- ✅ Image upload support
- ✅ JWT Authentication
- ✅ Pagination & filtering
- ✅ Clean code architecture (views, serializers, permissions)
- ✅ Admin panel with CKEditor support
- ✅ Dockerized for local development

---

## 📸 Admin Panel

![Use Case Diagram](img.png)

---

## 📦 Tech Stack

- **Python 3.10+**
- **Django 4.x**
- **Django Rest Framework**
- **django-ckeditor**
- **Simple JWT**
- **PostgreSQL** (or SQLite for development)
- **Docker & Docker Compose**

---

## 🧑‍💻 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/diaco-dev/drf-blog-with-ckeditor.git 
   cd drf-blog-with-ckeditor
  
2. **Create and activate virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate
     ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```
5. **Run development server**
   ```bash
   python manage.py runserver
   ```
