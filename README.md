# Provider and Client Management System

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.3-green?logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.20-red?logo=sqlalchemy)

A robust, scalable Python application designed for businesses to manage their products and enable customers to place purchase orders. Built with Flask and PostgreSQL, featuring clean architecture principles and containerized deployment.

## 🌟 Features

- **Provider Management**: Businesses can register products, update inventories, and manage pricing
- **Client Portal**: Customers can browse products, place orders, and track order status
- **Order Processing**: Complete order lifecycle management from placement to fulfillment
- **JWT Authentication**: Secure user authentication and authorization
- **RESTful API**: Well-structured API endpoints for all operations
- **Database Migrations**: Automated database schema management with Flask-Migrate
- **Soft Delete**: Data preservation with soft delete functionality
- **Environment Configurations**: Separate configurations for development, testing, and production

## 🛠️ Tech Stack

| Technology             | Purpose                       | Version |
| ---------------------- | ----------------------------- | ------- |
| **Python**             | Backend Programming Language  | 3.8+    |
| **Flask**              | Web Framework                 | 3.0.3   |
| **SQLAlchemy**         | ORM & Database Management     | 2.0.20  |
| **PostgreSQL**         | Primary Database              | Latest  |
| **Flask-SQLAlchemy**   | Flask-SQLAlchemy Integration  | 3.0.5   |
| **Flask-Migrate**      | Database Migration Tool       | 4.0.4   |
| **Flask-JWT-Extended** | JWT Authentication            | 4.6.0   |
| **Marshmallow**        | Serialization/Deserialization | 3.20.1  |
| **Passlib**            | Password Hashing              | 1.7.4   |
| **Docker**             | Containerization              | Latest  |

## 📁 Project Structure

```
provider-app/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── config/                  # Configuration management
│   │   ├── __init__.py
│   │   └── config.py           # Environment configurations
│   ├── controllers/            # Request handlers (MVC Controllers)
│   │   ├── __init__.py
│   │   ├── home_controller.py
│   │   ├── order_controller.py
│   │   ├── product_controller.py
│   │   └── user_controller.py
│   ├── models/                 # Database models (MVC Models)
│   │   ├── __init__.py
│   │   ├── order.py
│   │   ├── product.py
│   │   └── user.py
│   ├── repositories/           # Data access layer
│   │   ├── __init__.py
│   │   ├── base_repository.py
│   │   ├── order_repository.py
│   │   ├── product_repository.py
│   │   └── user_repository.py
│   ├── services/               # Business logic layer
│   │   ├── __init__.py
│   │   ├── actions_services.py
│   │   ├── message.py
│   │   ├── order_services.py
│   │   ├── product_services.py
│   │   ├── security_manager.py
│   │   ├── security.py
│   │   └── user_services.py
│   ├── mapping/                # Data transformation layer
│   │   ├── __init__.py
│   │   ├── message_mapping.py
│   │   ├── order_mapping.py
│   │   ├── product_mapping.py
│   │   └── user_mapping.py
│   ├── routes/                 # URL routing
│   │   ├── __init__.py
│   │   └── routes.py
│   └── route/                  # Route configuration
│       ├── __init__.py
│       └── route.py
├── test/                       # Test suite
│   ├── __init__.py
│   ├── test_app.py
│   ├── test_db.py
│   ├── test_order.py
│   ├── test_product.py
│   └── test_user.py
├── docs/                       # Documentation & UML diagrams
│   ├── casosUso.puml
│   ├── diagramaClases.puml
│   └── diagramaSecuencias.puml
├── app.py                      # Application entry point
├── requirements.txt            # Python dependencies
├── boot.ps1                    # Windows startup script
├── installs.ps1               # Installation script
└── README.md                   # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- **Python** (version 3.8 or higher)
- **PostgreSQL** (or Docker for containerized database)
- **Docker & Docker Compose** (optional, for containerized deployment)
- **pip** package manager

### Installation

1. **Clone the repository**

   ```powershell
   git clone https://github.com/ElielMato/provider-app.git
   cd provider-app
   ```

2. **Create a virtual environment**

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**

   ```powershell
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory:

   ```env
   DEV_DATABASE_URI=postgresql://username:password@localhost/provider_app_dev
   TEST_DATABASE_URI=postgresql://username:password@localhost/provider_app_test
   PROD_DATABASE_URI=postgresql://username:password@localhost/provider_app_prod
   JWT_SECRET_KEY=your-secret-key-here
   FLASK_ENV=development
   ```

5. **Initialize the database**

   ```powershell
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. **Run the application**

   ```powershell
   python app.py
   ```

7. **Access the application**

   Navigate to `http://localhost:5000` to see the application running.

## 🐳 Docker Deployment

### Using Docker Compose

1. **Build and run with Docker Compose**

   ```powershell
   docker-compose up --build
   ```

2. **Run in detached mode**

   ```powershell
   docker-compose up -d
   ```

3. **Stop the services**

   ```powershell
   docker-compose down
   ```

## 🏗️ Development

### Running Tests

```powershell
# Run all tests
python -m pytest test/

# Run specific test file
python -m pytest test/test_user.py

# Run with coverage
python -m pytest --cov=app test/
```

### Database Operations

```powershell
# Create a new migration
flask db migrate -m "Description of changes"

# Apply migrations
flask db upgrade

# Rollback migration
flask db downgrade
```

## 🔧 Architecture & Design Patterns

- **MVC Architecture**: Clear separation of concerns with Models, Views (Controllers), and business logic
- **Repository Pattern**: Abstracted data access layer for better testability and maintainability
- **Service Layer**: Business logic encapsulation separate from controllers
- **Factory Pattern**: Efficient object creation and configuration management
- **Singleton Pattern**: Database connection management
- **SOLID Principles**: Applied throughout the codebase for maintainability and extensibility

## 📚 API Documentation

The application provides RESTful API endpoints for:

- **Authentication**: User registration, login, and JWT token management
- **Users**: User profile management and CRUD operations
- **Products**: Product catalog management for providers
- **Orders**: Order placement, tracking, and management

## 🧪 Testing

The project includes comprehensive tests covering:

- Unit tests for models, services, and repositories
- Integration tests for API endpoints
- Database operation tests
- Authentication and authorization tests

## 📝 License

This project is proprietary software developed for Provider and Client Management System. All rights reserved.

---

<div align="center">

**Built with ❤️ using Python, Flask, and modern software engineering practices**

</div>
