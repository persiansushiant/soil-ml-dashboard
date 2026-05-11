# API Documentation

## Overview

The Soil ML Dashboard currently exposes a lightweight API-style workflow through Flask routes and dashboard parameters.

The application architecture is intentionally designed so that future REST API endpoints can be added with minimal restructuring.

---

# Current Route

## Main Dashboard Route

```text
Renders the main dashboard interface.

Supported Query Parameters
country

Filter the dataset by country.

Example:

/?country=Sweden
soil_type

Filter the dataset by soil type.

Example:

/?soil_type=Clay
target

Select the machine learning target variable.

Example:

/?target=moisture
model

Select the regression model.

Example:

/?model=Random Forest
Combined Example
/?country=Sweden&soil_type=Clay&target=moisture&model=Random Forest
Machine Learning Workflow

When query parameters are provided, the application:

Loads the dataset
Applies filters
Selects numeric features
Trains the selected model
Generates predictions
Calculates benchmark metrics
Renders visualizations
Planned API Extensions

Potential future REST endpoints:

Dataset Endpoints
/api/data
/api/summary
/api/filters
Machine Learning Endpoints
/api/train
/api/benchmark
/api/models
Export Endpoints
/api/export/csv
/api/export/json
Future Improvements

Potential API improvements include:

JSON responses
authentication
PostgreSQL integration
asynchronous processing
model persistence
dataset upload endpoints
geospatial endpoints
satellite-data integration