# Usage Guide

## Installation

Install dependencies:

```bash
pip install -r requirements.txt


Running the Application

Start the Flask application:

python app.py

Open the dashboard in your browser:

http://127.0.0.1:5000
Dashboard Controls

The dashboard allows the user to:

Filter by country
Filter by soil type
Select a machine learning target
Choose a regression model
Run benchmark analysis
Available Models
Linear Regression
Decision Tree Regressor
Random Forest Regressor
Outputs

The dashboard generates:

Interactive charts
Performance metrics
Actual vs predicted plots
Model comparison visualizations

---

# docs/workflow.md

```md
# Workflow Overview

## Data Processing Workflow

1. Load soil data from CSV
2. Add derived risk-level categories
3. Apply user-selected filters
4. Prepare data for visualization
5. Generate dashboard charts

---

# Machine Learning Workflow

1. Select target variable
2. Select regression model
3. Extract numeric feature columns
4. Split dataset into train/test sets
5. Train model
6. Generate predictions
7. Calculate metrics
8. Compare models

---

# Dashboard Workflow

The Flask application:

- Receives user input
- Processes filters
- Runs machine learning analysis
- Generates Plotly visualizations
- Renders the dashboard template