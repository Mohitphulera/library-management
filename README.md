# Library Management System

A Django-based web application for managing a library, including features for user registration, book management, and transaction handling by administrators.

## Features

- User registration and authentication
- Book management (add, issue, return, and remove books)
- Admin and regular user roles

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/library-management-system.git
    cd library-management-system
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000/library/`.

## Usage

### User Registration

- Visit `/library/register/` to create a new account.
- After registering, you will be automatically logged in and redirected to the book list page.

