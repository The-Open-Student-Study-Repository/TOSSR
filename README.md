# TOSSR - The Open Student Study Repository

WAD2 Group Project - Group 5C

## Team Members
- Matthew MacPhail
- Guanjie Wang
- Kai Loach
- Ali N H A Algharabally
- Evan Cureton

## PythonAnywhere Deployment
[Link to TOSSR Deployment](https://matthewjmacphail.eu.pythonanywhere.com/)
## Description
A web platform for students to share and discover module specific study materials including flashcards and quizzes.
This software is currently intended to be used by Universioty of Glasgow Students only.

## Prerequisites
- Python 3.10+ (Project developed with Python 3.14)
  - [Download Python](https://www.python.org/downloads/)
- MariaDB or MySQL database server
  - **Windows:** [Download MariaDB](https://mariadb.org/download/)
  - **macOS:** `brew install mariadb`
  - **Linux:** `sudo apt install mariadb-server` or `sudo pacman -S mariadb`  (Varies by distro)
- Git
## Local Setup

1. Clone the repository:
```bash
   git clone https://github.com/yourusername/TOSSR.git
   cd TOSSR
```

2. Create virtual environment:
```bash
   python -m venv .venv
   source .venv/bin/activate  # On Fish: . .venv/bin/activate.fish
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Set up environment variables:
```bash
   cp .env.example .env
   # Edit .env with your local MariaDB credentials
```

5. Create database in MariaDB:
```sql
   CREATE DATABASE tossr_db;
   CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON tossr_db.* TO 'your_username'@'localhost';
```

6. Run migrations:
```bash
   python manage.py migrate
```

7. Run development server:
```bash
   python manage.py runserver
```

## Technologies Used (WIP)
- Python/Django
- MariaDB
- Bootstrap
- JavaScript/jQuery/AJAX

By contributing to this project, you agree to the terms in .github/CLA.md
