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

---

## Authentication & Authorization

---

## API Documentation

---

## Deployment

---

## Git Workflow
