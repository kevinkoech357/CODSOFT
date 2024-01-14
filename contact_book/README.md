# Contact Management API

The Contact Management API is a Flask application designed for managing contacts. It provides a RESTful API for performing operations related to authentication, user management, and contact management.

## Features

- User authentication and registration.
- CRUD operations for managing contacts.
- Integrated Swagger documentation using Flask-RESTx.

## Getting Started

To run the Contact Management API, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/kevinkoech357/CODSOFT.git
    ```

2. Navigate to the project and set it up:

    ```bash
    cd CODSOFT
    # Create virtual env
    python3 -m venv env
    source env/bin/activate
    # Install extensions
    pip install -r requirements.txt
    # Navigate to project
    cd contact_book
    ```

3. Set up the database:

    ```bash
    flask db upgrade
    ```

4. Run the application:

    ```bash
    python run.py
    ```

6. Open your web browser and visit [http://localhost:5000](http://localhost:5000).

## Project Structure

```plaintext
├── app
│   ├── aid
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── auth
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── config.py
│   ├── __init__.py
│   ├── models
│   │   ├── contacts.py
│   │   ├── __init__.py
│   │   └── user.py
│   ├── user
│   │   ├── __init__.py
│   │   └── routes.py
│   └── utils.py
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── __pycache__
│   │   └── env.cpython-311.pyc
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── b11c0bbb0cad_update_time.py
│       ├── df5612cbc57a_update_contacts_table.py
│       └── __pycache__
├── README.md
└── run.py
```
