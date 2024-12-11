# Provider and Client App

This is a Python application that allows businesses to manage their products and customers to place purchase orders. The system is designed to be flexible, scalable, and easy to maintain, utilizing proper design principles and patterns for operating system applications.

The project uses a PostgreSQL database and is fully configured to run in a Docker environment.

## Features

- **Providers**: Businesses can register their products, update inventories, and manage prices.
- **Clients**: Customers can place purchase orders, view available products, and check the status of their orders.
- **Order Management**: Customers can make purchases, and providers can view and process orders.
  
## Technologies

- **Backend**: Python
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Design Patterns**:
  - **MVC** (Model-View-Controller): Clear separation of concerns within the application.
  - **Singleton**: Ensures only one instance of the database connection is active.
  - **Factory**: Efficient object creation for products and orders.
- **SOLID Principles**: Applied to ensure the code is modular, maintainable, and extensible.

## Requirements

To run this application, you will need the following:

- Docker
- Docker Compose
- Python 3.8 or higher
