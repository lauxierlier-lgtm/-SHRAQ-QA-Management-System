# SHRAQ – QA Management System

A Django-based Quality Assurance and Bug Tracking Management System designed to organize software testing activities, manage projects, track bugs, and maintain test cases.

## About the Project

SHRAQ is a web-based application developed to simplify software quality assurance and project management.

It provides a centralized platform where users can manage testing projects, record software defects, and organize test cases.

## Features

- User Registration and Login
- User Dashboard
- Project Management
- Bug Tracking
- Bug Severity and Status Management
- Test Case Management
- Secure User Authentication

## Technologies Used

- Python 3.12
- Django 6.1.3
- SQLite
- HTML5
- CSS3
- JavaScript
- Visual Studio Code
- Git and GitHub

## Project Structure

```text
BugTrack/
│
├── accounts/
│   ├── templates/
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/
│   ├── templates/
│   ├── migrations/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── manage.py
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/lauxierlier-lgtm/-SHRAQ-QA-Management-System.git
```

### 2. Open the project folder

```bash
cd -SHRAQ-QA-Management-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Django

```bash
pip install django
```

### 6. Configure the secret key

In PowerShell, set a new Django secret key:

```powershell
$env:DJANGO_SECRET_KEY = python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 7. Apply migrations

```bash
python manage.py migrate
```

### 8. Run the development server

```bash
python manage.py runserver
```

Open your browser:

http://127.0.0.1:8000/

## Developer

Developed as a software quality assurance and bug tracking management project.

## Project Status

Under Development.