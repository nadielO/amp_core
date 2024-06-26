# backend_amp_core

This project, "backend_amp_core," is a secure, scalable Python-based web application built using FastAPI. It is designed to provide a RESTful API with user management capabilities, JWT-based authentication, and PostgreSQL database integration. The application is containerized using Docker, promoting consistent environments across development and production setups.

## Overview

The application architecture is modular, employing FastAPI for the API layer, SQLAlchemy for ORM, and PostgreSQL for the database. It follows a clean separation of concerns with distinct layers for API endpoints, business logic, data models, and database operations. The project is structured into various directories to maintain a manageable and organized codebase.

### Technologies Used
- **Python**: Programming language for building the application.
- **FastAPI**: Modern, high-performance web framework for building APIs.
- **PostgreSQL**: Relational database system.
- **Docker**: Platform for containerization.
- **Uvicorn**: ASGI server for Python, used to run FastAPI.
- **SQLAlchemy**: SQL toolkit and ORM system for Python.
- **Alembic**: Database migration tool.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **python-jose**: JOSE implementation in Python for JWT handling.

### Project Structure
- `app/`: Main application directory with subdirectories for API, core functionalities, database interactions, models, schemas, and services.
- `alembic/`: Contains Alembic configurations and migration scripts.
- `scripts/`: Utility scripts for deployment and startup.
- Configuration files like `.env`, `.gitignore`, `alembic.ini`, `Dockerfile`, `docker-compose.yml`, and `requirements.txt`.

## Features
- **User Management**: Supports CRUD operations on user data.
- **Authentication**: Uses JWT for secure authentication.
- **API Versioning**: Easily extendable API versioning starting with v1.
- **Database Integration and Migrations**: Integrated with PostgreSQL and managed via Alembic.
- **Testing and Security**: Includes a comprehensive testing setup and prioritizes security through configurations and JWT.

## Getting Started

### Requirements
- Python 3.6+
- Docker and Docker Compose
- PostgreSQL

### Quickstart
1. Clone the repository to your local machine.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the PostgreSQL database and modify the `.env` file with the appropriate database credentials.
4. Run the database migrations:
   ```bash
   alembic upgrade head
   ```
5. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```
6. Access the application at `http://localhost:8000/api/v1/`.

### License
Copyright (c) 2024. All rights reserved.

The project is proprietary and not open source. Unauthorized copying of files, via any medium, is strictly prohibited.