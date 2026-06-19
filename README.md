# Sales Forecasting Business Intelligence Platform

An end-to-end Business Intelligence (BI) and predictive analytics platform built with Django. The system ingests historical sales data via REST APIs, processes it through a secure backend architecture, and delivers machine learning-driven sales forecasts alongside critical financial KPIs.
## 🏗️ System Architecture

The data flows through the backend ecosystem following this pipeline:


  Django Project
        │
        ▼
  SQLite Database
        │
        ▼
   Sales Model
        │
        ▼
  Django Admin Panel
        │
        ▼
    Serializer
        │
        ▼
    REST API

## 🛠️ Tech Stack

* Backend Framework: Django, Django REST Framework (DRF)
* Database: SQLite (Development/Default)
* Authentication: Simple JWT (JSON Web Tokens)
* Machine Learning / Analytics: Prophet, XGBoost, Pandas, NumPy


## 🔌 API Documentation & Endpoints

All core data endpoints require valid **JWT Authentication**. Secure your requests by including the token in your headers: `Authorization: Bearer <your_token>`.

### 📦 Core Sales Operations

* `GET /api/sales/` - Retrieves a paginated list of all historical sales records.
* `POST /api/sales/` - Handles bulk **CSV upload** to easily ingest high-volume historical transactions into the database.

### 📊 Business Intelligence & Analytics

* `GET /api/sales/analytics/` - Provides parsed, aggregated data points optimized for rendering charts and trendlines.
* `GET /api/sales/revenue-kpi/` - Exposes high-level metrics (Total Revenue, Gross Profit Margin, MoM Growth) to feed front-end BI scorecards.

### 🔮 Machine Learning Forecasting

* `GET /api/sales/forecast/prophet/` - Generates time-series predictions leveraging Meta's **Prophet** model to capture seasonality and holiday trends.
* `GET /api/sales/forecast/xgboost/` - Generates high-performance regression-based sales forecasts utilizing structural features with **XGBoost**.


## 📁 Project Structure

```text
├── core_project/          # Django project configuration settings
├── sales_api/             # Core application directory
│   ├── models.py          # Sales Model schema definitions
│   ├── serializers.py     # Serializers for transforming DB queries to JSON
│   ├── views.py           # API views handling business & ML logic
│   └── urls.py            # Routing for /api/sales/* endpoints
├── data/                  # Sample data and CSV templates
├── requirements.txt       # Python library dependencies
└── README.md              # Project documentation


## ⚙️ Quick Start

1. Clone & Set Up Environment
git clone https://github.com/RuchikaN2801/Sales-Forecasting-Business-Intelligence-Platform.git
cd Sales-Forecasting-Business-Intelligence-Platform

1.1 Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

2. Install Dependencies
pip install -r requirements.txt

3. Initialize Database & Admin
python manage.py migrate
python manage.py createsuperuser  # Access the Django Admin Panel here

4. Run the Server
python manage.py runserver

