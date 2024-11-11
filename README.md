# SSYS Employee Manager

A robust FastAPI application for employee management, built with clean architecture principles and modern Python practices. This project was developed as part of the SSYS job application process.

## Try it Out

The application is deployed and ready to use:
- **Production URL**: https://ssys-challenge.gnlware.com
- **API Documentation**:
  - Swagger UI: https://ssys-challenge.gnlware.com/docs
  - ReDoc: https://ssys-challenge.gnlware.com/redoc

## Features

### Core Functionality
- **Employee Management**: Complete CRUD operations for employee records
- **User Management**: User system with authentication
- **Reporting System**: Reporting features with salary and age analytics
- **JWT Authentication**: Secure endpoints with JSON Web Token authentication
- **Async Operations**: Built with asyncio and SQLAlchemy async for optimal performance
- **PostgreSQL Database**: Reliable data persistence with PostgreSQL

### Technical Highlights
- Clean Architecture with Domain-Driven Design (DDD)
- Dependency Injection pattern
- FastAPI for high-performance async API
- SQLAlchemy for async database operations
- Alembic for database migrations
- Docker and Docker Compose for containerization

## Project Structure
```
ssys-manager/
├── alembic/                          # Database migrations
├── api/
│   └── v1/
│       ├── routes/
│       │   ├── auth_routes.py         # Authentication endpoints
│       │   ├── employee_routes.py     # Employee CRUD endpoints
│       │   ├── employee_reports_routes.py  # Reporting endpoints
│       │   └── user_routes.py         # User CRUD endpoints
│       └── middlewares/
│           └── auth_middleware.py      # JWT authentication
├── application/
│   └── services/
│       ├── auth_service.py             # Service layers for business logic
│       ├── employee_service.py
│       ├── employee_reports_service.py
│       └── user_service.py
├── domain/
│   └── entities/
│       ├── employee.py
│       ├── user.py
│       └── auth.py
├── infrastructure/
│   ├── repositories/
│   │   ├── employee_repository.py      # Repository pattern for data access
│   │   └── user_repository.py          
│   └── database/
│       └── connection.py
│       └── models.py                   # SQLAlchemy models
└── core/
│   └── di/
│       └── services.py                 # Dependency injection
│       └── repositories.py             
│       └── database.py
└── main.py                             # FastAPI application             
```

## API Endpoints

### Authentication
```
POST /auth/login - Authenticate user and receive JWT token
```

### Employee Management
```
GET    /employees/     - List all employees
POST   /employees/     - Create new employee
GET    /employees/{id} - Get employee details
PUT    /employees/{id} - Update employee
DELETE /employees/{id} - Delete employee
```

### Reports
```
GET /reports/employees/salary/ - Salary analytics report
GET /reports/employees/age/    - Age demographics report
```

### User Management
```
POST   /users/     - Create new user
GET    /users/     - List all users
GET    /users/{id} - Get user details
PUT    /users/{id} - Update user
DELETE /users/{id} - Delete user
```

## Installation & Setup

### Local Development with Docker

1. Clone the repository:
```bash
git clone git@github.com:DenLopes/ssys-challenge.git
cd ssys-manager
```

2. Start the Docker containers:
```bash
docker-compose up -build
```

3. Run initial database migrations:
```bash
# Enter the application container
docker exec -it <container-id> bash

# Run migrations
alembic upgrade head

# Exit the container
exit
```

## Local Documentation
Once running locally, API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Development Notes

### Authentication Flow
- JWT-based authentication system
- Token required for all protected endpoints
- Middleware handles token validation

### Database Management
- Async SQLAlchemy for database operations
- Alembic handles database migrations
- PostgreSQL for data persistence

### Architecture Decisions
- DDD pattern for clear separation of concerns
- Service layer pattern for business logic
- Repository pattern for data access
- Dependency injection for loose coupling

## Author
Denis Lopes - [GitHub Profile](https://github.com/DenLopes)