# Database Design for E-Commerce Platform

This project demonstrates a Django-based implementation of an e-commerce database design. It showcases the creation of models, views, and templates to manage various aspects of an online store.

## 📦 Features

- **Product Catalog**: Manage product listings, categories, and details.
- **Inventory Management**: Track stock levels and product availability.
- **User Authentication**: Secure login and registration for customers and admins.
- **Order Processing**: Handle customer orders, payments, and order status.
- **Admin Dashboard**: Admin interface to manage products, orders, and users.

## 🛠️ Technologies Used

- **Backend**: Django (Python)
- **Database**: SQLite (default), can be configured to use PostgreSQL or MySQL
- **Frontend**: HTML, CSS, JavaScript (Bootstrap)
- **Testing**: Pytest

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Django 3.x or higher
- pip (Python package installer)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/TyroneZeka/Database-Design-Ecommerce.git
   cd Database-Design-Ecommerce
2. Create a virtual env:
   ```bash
   python -m venv venv
   source venv/bin/activate # on windows it's venv/Scripts/activate
3. Install required packages
   ```bash
   pip install =r requirements.txt
4. Apply database migrations
   ```bash
    python manage.py migrate
5. Create a superuser for admin panel
    ```bash
    python manage.py createsuperuser
6. Run deployment serer
   ```bash
    python manage.py runserver
7. Access the application at `localhost:8000` and the admin panel at `localhost:8000/admin/`

## Contribution
Contributions are welcome!Please fork the repository and create a new branch, and submit a pull request with a description of your changes.

## Licence
The project is licensed under the MIT Licence.
