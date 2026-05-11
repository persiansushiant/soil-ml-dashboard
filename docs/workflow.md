# Workflow Overview

## Overview

The Soil ML Dashboard follows a lightweight environmental-data analysis workflow designed for interactive exploration and machine learning benchmarking.

The workflow combines:

- data loading
- filtering
- feature engineering
- visualization
- machine learning
- dashboard rendering

---

## High-Level Workflow

```text
User Input
    ↓
Dataset Loading
    ↓
Filtering & Feature Engineering
    ↓
Visualization Generation
    ↓
Machine Learning Benchmark
    ↓
Metric Calculation
    ↓
Dashboard Rendering
```

---

## Step 1: Dataset Loading

The application loads soil-health data from a CSV dataset.

Location:

```text
data/soil_data.csv
```

The dataset includes variables such as:

- soil moisture
- temperature
- pH
- organic carbon
- nitrogen
- soil type
- country
- geographic location

---

## Step 2: Feature Engineering

During loading, additional derived features are generated.

Example:

### Soil Risk Classification

The application creates a derived:

```text
risk_level
```

column based on soil moisture values.

Example categories:

- High Risk
- Medium Risk
- Low Risk

This workflow demonstrates lightweight feature engineering inside the dashboard pipeline.

---

## Step 3: Dataset Filtering

Users can interactively filter the dataset by:

- country
- soil type

The filtering process dynamically updates:

- charts
- summary statistics
- machine learning workflows

---

## Step 4: Visualization Workflow

The dashboard generates interactive Plotly visualizations.

Current visualizations include:

### Scatter Plot

Temperature vs moisture.

### Bar Chart

Average moisture per country.

### Histogram

Organic carbon distribution.

### Risk-Level Analysis

Counts of soil-risk categories.

---

## Step 5: Machine Learning Workflow

Users can select:

- a target variable
- a regression model

The workflow then:

1. extracts numeric features
2. splits the dataset into train/test sets
3. trains the selected model
4. generates predictions
5. calculates benchmark metrics

---

## Supported Models

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

## Step 6: Benchmark Metrics

The dashboard calculates:

| Metric | Purpose |
|---|---|
| MAE | Mean Absolute Error |
| RMSE | Root Mean Squared Error |
| R² | Explained variance / model fit |

---

## Step 7: Prediction Visualization

The machine learning workflow generates:

- actual vs predicted plots
- model comparison charts
- benchmark metric tables

This allows rapid comparison of model performance.

---

## Step 8: Dashboard Rendering

The Flask application renders:

- charts
- statistics
- tables
- benchmark results

using:

- Jinja templates
- Plotly HTML components
- modular utility modules

---

## Modular Workflow Design

The project separates responsibilities into reusable modules.

### data_utils.py

Handles:

- data loading
- filtering
- feature engineering

### ml_utils.py

Handles:

- model creation
- training
- benchmarking
- metric calculation

### chart_utils.py

Handles:

- Plotly chart generation
- reusable visualizations

---

## Design Goals

The workflow prioritizes:

- modularity
- readability
- lightweight deployment
- educational clarity
- reusable analytics workflows

---

## Future Workflow Extensions

Potential future workflow improvements include:

- PostgreSQL integration
- CSV upload support
- satellite-data integration
- geospatial analysis
- Docker deployment
- asynchronous processing
- REST API workflows
- exportable benchmark reports