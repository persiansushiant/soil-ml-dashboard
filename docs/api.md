# API Documentation

## Overview

The Soil ML Dashboard currently exposes a lightweight API-style workflow through Flask routes and dashboard parameters.

The application architecture is intentionally designed so that future REST API endpoints can be added with minimal restructuring.

---

## Main Dashboard Route

```text
/
```

Renders the main dashboard interface.

---

## Supported Query Parameters

### country

Filter the dataset by country.

Example:

```text
/?country=Sweden
```

---

### soil_type

Filter the dataset by soil type.

Example:

```text
/?soil_type=Clay
```

---

### target

Select the machine learning target variable.

Example:

```text
/?target=moisture
```

---

### model

Select the regression model.

Example:

```text
/?model=Random Forest
```

---

## Combined Example

```text
/?country=Sweden&soil_type=Clay&target=moisture&model=Random Forest
```

---

## Machine Learning Workflow

When query parameters are provided, the application:

1. loads the dataset
2. applies filters
3. selects numeric features
4. trains the selected model
5. generates predictions
6. calculates benchmark metrics
7. renders visualizations

---

## Planned API Extensions

Potential future REST endpoints:

### Dataset Endpoints

```text
/api/data
/api/summary
/api/filters
```

---

### Machine Learning Endpoints

```text
/api/train
/api/benchmark
/api/models
```

---

### Export Endpoints

```text
/api/export/csv
/api/export/json
```

---

## Future Improvements

Potential API improvements include:

- JSON responses
- authentication
- PostgreSQL integration
- asynchronous processing
- model persistence
- dataset upload endpoints
- geospatial endpoints
- satellite-data integration