# Sales Forecasting & Business Intelligence Platform

## Overview

A Django REST Framework based Sales Forecasting and Business Intelligence Platform that enables organizations to ingest sales data, perform business analytics, and generate future revenue forecasts using Machine Learning models.

The platform provides secure JWT authentication, REST APIs, sales analytics, revenue trend monitoring, CSV-based bulk data upload, and forecasting using Prophet and XGBoost.

---

## Features

### Authentication & Security

* JWT Authentication using SimpleJWT
* Protected API endpoints
* Secure token-based access control

### Sales Management

* Create sales records
* View sales records
* Update sales records
* Delete sales records
* Automatic revenue calculation

### CSV Data Upload

* Bulk sales data upload through CSV files
* Automated database insertion
* Revenue generation from uploaded data

### Business Analytics

* Total Revenue Analysis
* Total Quantity Sold
* Best Selling Product Identification
* Product-wise Performance Tracking

### Revenue Trend Analysis

* Historical revenue trend visualization
* Time-series sales monitoring

### Machine Learning Forecasting

#### Prophet Forecasting

* Time-series forecasting
* Future revenue prediction
* Trend analysis

#### XGBoost Forecasting

* Machine Learning based revenue forecasting
* Future sales estimation
* Predictive business analytics

### API Documentation

* Swagger UI Integration
* ReDoc Documentation
* Interactive API Testing

---

## Technology Stack

### Backend

* Python
* Django
* Django REST Framework

### Database

* SQLite

### Authentication

* JWT (SimpleJWT)

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Prophet
* XGBoost
* Scikit-Learn

### API Documentation

* drf-yasg (Swagger)

---

## System Architecture

CSV Upload
↓
Django REST APIs
↓
Sales Database
↓
Analytics Engine
↓
Forecasting Models
↓
Business Insights

---

## API Endpoints

### Authentication

POST /api/token/

POST /api/token/refresh/

### Sales Management

GET /api/sales/

POST /api/sales/

GET /api/sales/{id}/

PUT /api/sales/{id}/

DELETE /api/sales/{id}/

### Data Upload

POST /api/upload-csv/

### Analytics

GET /api/analytics/

GET /api/revenue-trend/

### Forecasting

GET /api/forecast/

GET /api/xgboost-forecast/

### Documentation

GET /swagger/

GET /redoc/

---

## Project Highlights

* Developed secure RESTful APIs using Django REST Framework.
* Implemented JWT-based authentication and authorization.
* Designed analytics APIs for revenue and product performance tracking.
* Built machine learning forecasting pipelines using Prophet and XGBoost.
* Created automated CSV ingestion workflow for sales data processing.
* Integrated Swagger documentation for API testing and developer experience.

---

## Future Enhancements

* PostgreSQL Integration
* AWS Deployment
* Power BI Dashboard Integration
* Role-Based Access Control (RBAC)
* Automated Report Generation
* Docker Containerization

---

## Author

Ruchika Navrange

LinkedIn:
https://www.linkedin.com/in/ruchika-navrange-935a04257
