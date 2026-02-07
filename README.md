# ALX Backend Nexus: Property Insurance Backend System
*By: Hilda Enyioko*

---

## Overview

This project is a **Property Insurance Backend System** designed to simulate a real-world e-commerce backend architecture.

The system manages insurance plans in a product-catalog-like structure, enabling users to browse, filter, and subscribe to insurance plans while administrators manage plans and categories. It emphasizes scalability, security, performance, and clean API design, aligning with the ALX ProDev Backend requirements.

---

## Project Objectives

- Design and implement a scalable backend system using Django and PostgreSQL
- Build secure CRUD APIs for insurance plans and property categories
- Implement filtering, sorting, and pagination for efficient plan discovery
- Optimize database performance using indexing and query optimization
- Secure APIs using JWT authentication
- Document APIs using Swagger/OpenAPI
- Deploy the application using containerized infrastructure

---

## Product Scope

The Property Categories covered in this project are:

1. **Residential Properties (Primary Focus):**
    - Apartments/Flats
    - Detached Houses
    - Duplexes
    - Bungalows

2. **Small Commercial Properties (Secondary Focus):**
    - Small offices
    - Shops / retail spaces

---

## System Architecture
The backend follows a modular monolith architecture built with Django and Django REST Framework, structured to allow future scaling into microservices if required.

### Architecture Layers:
- **Presentation Layer:**
    - RESTful APIs built with Django REST Framework
    - JSON-based request/response handling
    - Swagger/OpenAPI for API exploration and testing

- **Application Layer**
    - Business logic handled via service-oriented views and serializers
    - Validation, filtering, pagination, and permissions applied here

- **Domain Layer**
    - Core domain models: InsurancePlan, PropertyCategory, PolicySubscription
    - Enums for coverage levels, user roles, and subscription status

- **Data Layer**
    - PostgreSQL as the primary database
    - Indexed fields for high-performance querying
    - Django ORM for data access and migrations

- **Security Layer**
    - JWT-based authentication
    - Role-based access control (Admin vs User)
    - Protected endpoints for sensitive operations

---

## Database Design & Optimization

### 1️⃣ User (Policy Holder / Admin)

Extends Django's built-in User model.

| Field | Type| Notes |
| --- | --- | --- |
| id | UUID / Integer | Primary Key |
| username | String | Unique |
| email | Email | Unique |
| password | Hashed | Django default |
| role | Enum | ADMIN, USER |
| is_active | Boolean | Default true |
| date_joined | DateTime | Auto |

**📌 Relationship**
- One User → Many PolicySubscriptions

  
### 2️⃣ PropertyCategory

Represents the type of property (this is your product category).

| Field | Type| Notes |
| --- | --- | --- |
| id | UUID / Integer | Primary Key |
| name | String | Apartment, House, Duplex |
| description | Text | Optional |
| created_at | DateTime | Auto |

**📌 Relationship**
- One Category → Many InsurancePlans

  
### 3️⃣ InsurancePlan (Core “Product”)
This is the e-commerce product equivalent.

| Field | Type| Notes |
| --- | --- | --- |
| id | UUID / Integer | Primary Key |
| name | String | Plan name |
| property_category | FK | → PropertyCategory |
| coverage_level | Enum | Basic, Standard, Premium |
| coverage_amount | Decimal | Amount covered |
| premium | Decimal | Price |
| duration_months | Integer | in multiples of 6 (6, 12, 24, ...) |
| description | Text | Coverage details |
| is_active | Boolean | For soft removal |
| created_at | DateTime | Auto |

**📌 Indexes (important)**
- premium
- property_category
- coverage_level
  
**📌 Relationship**
- One InsurancePlan → Many PolicySubscriptions


### 4️⃣ PolicySubscription (Order / Purchase)
This represents a user subscribing to a plan.

| Field | Type| Notes |
| --- | --- | --- |
| id | UUID / Integer | Primary Key |
| user | FK | → User |
| insurance_plan | FK | → InsurancePlan |
| start_date | Date | Auto |
| end_date | Date | Calculated |
| status | Enum | Active, Expired, Cancelled |
| created_at | DateTime | Auto |

**📌 Relationship**
- Many subscriptions → One User
- Many subscriptions → One InsurancePlan

### Relationship Summary (Plain English)

User
 └───< PolicySubscription >─── InsurancePlan
                                      │
                                      └─── PropertyCategory
                                      
- A User can subscribe to many insurance plans
- An InsurancePlan belongs to one property category
- A PropertyCategory groups many insurance plans

---

## API Endpoints
### Authentication
| Method | Endpoint | Description |
| --- | --- | --- |
| POST | /api/auth/register/ | Register a new user |
| POST | /api/auth/login/ |	Authenticate user and return JWT |
| POST | /api/auth/refresh/ | Refresh access token |

### Property Categories
| Method | Endpoint | Access | Description |
| --- | --- | --- | --- |
| GET | /api/categories/ | Public | List all property categories |
| POST | /api/categories/ | Admin | Create a new category |
| GET | /api/categories/{id}/ | Public | Retrieve category details |
| PUT | /api/categories/{id}/ | Admin | Update category |
| DELETE | /api/categories/{id}/ | Admin | Soft delete category |

### Insurance Plans
| Method | Endpoint | Access | Description |
| --- | --- | --- | --- |
| GET |	/api/plans/ | Public | List insurance plans (filterable) |
| POST | /api/plans/ | Admin | Create a new insurance plan |
| GET | /api/plans/{id}/ | Public | Retrieve plan details |
| PUT | /api/plans/{id}/ | Admin | Update insurance plan |
| DELETE | /api/plans/{id}/ | Admin | Soft delete insurance plan |

#### Filtering & Query Parameters
- property_category
- coverage_level
- min_premium
- max_premium
- ordering=premium
- page, page_size

### Policy Subscriptions
| Method | Endpoint | Access | Description |
| --- | --- | --- | --- |
| POST | /api/subscriptions/ | Authenticated | Subscribe to an insurance plan |
| GET | /api/subscriptions/	| Authenticated | View user subscriptions |
| GET | /api/subscriptions/{id}/ | Owner/Admin	| View subscription details |
| PATCH	| /api/subscriptions/{id}/cancel/ | Owner | Cancel active subscription |

---

## Authentication & Authorization
### Authentication:
JWT-based authentication using access and refresh tokens

### Authorization Rules:
- Admins:
    - Manage categories and insurance plans
    - View all subscriptions
- Users:
    - Browse insurance plans
    - Subscribe to plans
    - View and manage their own subscriptions

### Security Measures:
- Password hashing via Django’s authentication system
- Protected endpoints using permission classes
- Role-based access control enforced at the view level

---

## API Documentation
The API is fully documented using Swagger / OpenAPI.
- **Swagger UI:** /api/docs/
- **Features:**
    - Interactive endpoint testing
    - JWT authentication support
    - Request/response schemas
    - Validation error previews

---

## Deployment
The application is deployed using containerized infrastructure for consistency and scalability.

**Deployment Stack:**
- Docker & Docker Compose
- Django + Gunicorn
- PostgreSQL
- Environment-based configuration

**Deployment Steps:**
- Clone the repository
- Configure environment variables
- Build Docker images
- Run database migrations
- Start services using Docker Compose

The backend is hosted on a cloud platform and is production-ready with proper logging, security, and performance optimizations.

