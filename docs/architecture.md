# Application Architecture

## Overview

The Soil ML Dashboard is designed as a lightweight modular research-tool prototype.

The application separates responsibilities into reusable utility modules in order to improve:

- readability
- maintainability
- extensibility
- documentation quality

---

## High-Level Architecture

```text
Browser
   ↓
Flask Routes
   ↓
Utility Modules
   ↓
Data Processing / ML / Visualization
   ↓
Rendered Dashboard
```

---

## Project Structure

```text
soil-ml-dashboard/
│
├── app.py
│
├── data/
│   └── soil_data.csv
│
├── src/
│   ├── data_utils.py
│   ├── ml_utils.py
│   └── chart_utils.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── css/
│       └── style.css
│
└── docs/
```

---

## Flask Layer

The Flask application handles:

- routes
- user requests
- filter parameters
- template rendering

The Flask layer intentionally contains minimal business logic.

---

## Data Layer

### data_utils.py

Responsible for:

- CSV loading
- feature engineering
- risk classification
- filtering operations
- filter-option generation

---

## Machine Learning Layer

### ml_utils.py

Responsible for:

- model creation
- train/test splitting
- regression workflows
- prediction generation
- benchmark comparison
- metric calculation

Supported models:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

## Visualization Layer

### chart_utils.py

Responsible for:

- Plotly chart creation
- reusable visualization functions
- dashboard chart generation

---

## Frontend Layer

### HTML Templates

The dashboard frontend uses:

- Jinja templating
- reusable dashboard cards
- dynamic rendering
- interactive controls

---

## Styling Layer

### style.css

The CSS layer is separated from the HTML template in order to improve:

- readability
- maintainability
- frontend organization

---

## Design Goals

The architecture prioritizes:

- modularity
- readability
- educational clarity
- lightweight deployment
- rapid prototyping

---

## Potential Future Extensions

Possible future improvements include:

- PostgreSQL integration
- REST API endpoints
- geospatial visualization
- satellite-data workflows
- model persistence
- authentication
- CSV upload workflows
- Docker deployment