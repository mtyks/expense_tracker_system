# 💰 Expense Tracker System

A Django-based web application that helps users track and categorize their daily expenses. This system provides a clean and functional interface to log spending, monitor habits, and gain insights into financial activity.

---

## 📖 Table of Contents

- [🚀 Features](#-features)  
- [🛠 Tech Stack](#-tech-stack)  
- [📸 Web Example](#-web-example)  
- [📦 Installation Guide](#-installation-guide)  
- [🧪 Running Tests](#-running-tests)  
- [🧹 Code Linting with Ruff](#-code-linting-with-ruff)  
- [🤖 GitHub Actions](#-github-actions)  
- [👤 About the Developer](#-about-the-developer)

---


## 🚀 Features

- Add, edit, and delete expense entries
- Categorize expenses (e.g., Food, Transport, Utilities)
- View expenses filtered by date and category
- Responsive web UI built with Django templates
- Uses SQLite by default (easy to switch to PostgreSQL/MySQL)
- Code linting with [Ruff](https://github.com/astral-sh/ruff)
- Unit testing with Django’s built-in test framework

---

## 🛠 Tech Stack

- **Language**: Python 3.12
- **Framework**: Django
- **Database**: SQLite
- **Linting**: Ruff
- **Testing**: Django test runner
- **CI/CD**: GitHub Actions (optional)

---

## 📸 Web Example

### Our Logo
![Web Screenshot](https://github.com/mtyks/expense_tracker_system/blob/main/expense_tracker/static/images/brandicon.png)

### 1. Home
Summarize income and expenses according to the filter or a month by default.
![Web Screenshot](https://github.com/mtyks/expense_tracker_system/blob/main/expense_tracker/static/images/egHome.png)

### 2. Filter Tab
![Web Screenshot](https://github.com/mtyks/expense_tracker_system/blob/main/expense_tracker/static/images/egFilter.png)

### 3. Edit
![Web Screenshot](https://github.com/mtyks/expense_tracker_system/blob/main/expense_tracker/static/images/egEdit.png)

### 4. Delete
![Web Screenshot](https://github.com/mtyks/expense_tracker_system/blob/main/expense_tracker/static/images/egDelete.png)

### 5. Add
![Web Screenshot](https://github.com/mtyks/expense_tracker_system/blob/main/expense_tracker/static/images/egAdd.png)

### 6. Search
![Web Screenshot](https://github.com/mtyks/expense_tracker_system/blob/main/expense_tracker/static/images/egSearch.png)

### 7. About us
![Web Screenshot](https://github.com/mtyks/expense_tracker_system/blob/main/expense_tracker/static/images/egAbout.png)

---

## 📦 Installation Guide

### 1. Clone the repository
```bash
git clone https://github.com/mtyks/expense_tracker_system.git
cd expense_tracker_system
```
### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply database migrations
```bash
python manage.py migrate
```
### 5. Start the development server
```bash
python manage.py runserver
```
### 6. Open in browser
```bash
http://127.0.0.1:8000/
```
---

🧪 Running Tests
To run all tests:
```bash
python manage.py test
```
🧹 Code Linting with Ruff
Check code quality with:
```bash
ruff check .
```
Auto-fix issues with:
```bash
ruff check . --fix
```

🤖 GitHub Actions
This project can integrate with GitHub Actions for automated code checks. You can configure it using .github/workflows/lint.yml.

👤 About the Developer
Hi, I'm mtyks — a developer interested in building practical web tools using Python and Django. This project is a personal exploration into full-stack development, clean architecture, and scalable design. I'm open to feedback, ideas, or collaboration.


