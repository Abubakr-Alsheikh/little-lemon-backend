# Little Lemon Restaurant Backend - Meta Back-End Developer Capstone Project

This repository contains the backend code for the Little Lemon Restaurant application, developed as part of the Meta Back-End Developer Professional Certificate on Coursera. It's a Django-based REST API designed to handle menu management, bookings, and potentially other restaurant operations.

## Project Overview

This project was the capstone project for the Meta Back-End Developer Professional Certificate. It demonstrates the skills and knowledge acquired throughout the program, including:

*   **Django Framework:** Building robust and scalable web applications using the Django framework.
*   **Django REST Framework:** Creating RESTful APIs for seamless data exchange.
*   **Database Management:** Designing database models and interacting with databases (MySQL in this case) using Django's ORM.
*   **API Design and Development:** Implementing API endpoints for various functionalities, including GET, POST, PUT, and DELETE methods.
*   **Testing:** Writing unit tests to ensure code quality and reliability.
*   **Version Control:** Utilizing Git and GitHub for version control and collaboration.

## Features

The backend API currently supports the following features:

*   **Menu Management:**
    *   View a list of all menu items.
    *   Retrieve details of a specific menu item.
    *   Add new menu items.
    *   Update existing menu items.
    *   Delete menu items.
*   **Booking Management:**
    *   View all bookings.
    *   Create new bookings.
    *   Retrieve specific bookings
    *   Update bookings
    *   Delete bookings

## Technologies Used

*   **Python:** The primary programming language.
*   **Django:** The web framework for building the application.
*   **Django REST Framework:** The toolkit for building RESTful APIs.
*   **MySQL:** The relational database management system.
*   **VS Code:** Code editor
*   **Pip:** Package installer
*   **Git:** Version control system.
*   **GitHub:** Hosting platform for the repository.

## Getting Started

### Prerequisites

*   Python 3.8 or higher
*   MySQL server
*   pip (Python package installer)
*   Git
*   Virtual Environment (recommended)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/little-lemon-backend.git
    cd little-lemon-backend
    ```

    **Note**: Replace `your-username` with your GitHub username.

2. **Create and activate a virtual environment (recommended):**

    ```bash
    # On Windows
    python -m venv venv
    venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database:**

    *   Create a MySQL database named `littlelemon`.
    *   Update the `DATABASES` settings in `LittleLemon/LittleLemon/settings.py` with your MySQL credentials:

        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'littlelemon',
                'USER': 'your_mysql_user',
                'PASSWORD': 'your_mysql_password',
                'HOST': 'localhost',
                'PORT': '3306',
            }
        }
        ```

5. **Apply migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

### Running the Application

1. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

2. **Access the API:**

    The API will be accessible at `http://127.0.0.1:8000/`.

    The browsable API (Django REST Framework) will be available at:

    *   Menu items: `http://127.0.0.1:8000/restaurant/menu/`
    *   Bookings: `http://127.0.0.1:8000/restaurant/booking/tables/`

3. **Access the Django Admin:**
    The Django Admin interface will be available at `http://127.0.0.1:8000/admin`.

### Running Tests

```bash
python manage.py test
```

## Project Structure

*   **`LittleLemon/`:** Main project directory.
    *   **`LittleLemon/`:** Project settings and configuration.
    *   **`restaurant/`:** Django app for restaurant functionalities.
        *   **`migrations/`:** Database migration files.
        *   **`models.py`:** Database models (Menu, Booking).
        *   **`serializers.py`:** Serializers for converting data to JSON.
        *   **`views.py`:** API views.
        *   **`urls.py`:** URL routing for the app.
        *   **`admin.py`:** Admin configuration.
    *   **`tests/`:** Test files.
        *   **`test_models.py`:** Model tests.
        *   **`test_views.py`:** View tests.
*   **`manage.py`:** Django management script.
*   **`requirements.txt`:** List of project dependencies.
*   **`README.md`:** This file.

## Future Improvements

*   **Authentication and Authorization:** Implement user authentication and authorization to secure the API.
*   **User Roles:** Introduce different user roles (e.g., customer, manager, admin) with varying levels of access.
*   **Filtering and Sorting:** Add filtering and sorting capabilities to the API endpoints.
*   **Error Handling:** Implement more robust error handling and reporting.
*   **Email Integration:** Send booking confirmations and other notifications via email.
*   **Payment Gateway Integration:** Integrate a payment gateway for online payments.

## Acknowledgements

*   Meta Back-End Developer Professional Certificate Program
*   Coursera
*   Django and Django REST Framework communities.
