# Soil ML Dashboard

A Flask-based interactive dashboard for soil-health analytics, environmental visualization, and machine learning benchmarking.

This repository demonstrates a lightweight research-tool prototype inspired by scientific environmental workflows.

---

# Features

## Environmental Analytics

- Soil moisture exploration
- Organic carbon analysis
- Country-based filtering
- Soil-type filtering
- Risk-level classification

---

## Machine Learning Benchmarking

- Regression workflows
- Model comparison
- MAE, RMSE, and R² evaluation
- Actual vs predicted visualization
- Benchmark metrics dashboard

Supported models:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

---

# Technology Stack

| Layer | Technology |
|---|---|
| Backend | Flask |
| Data Processing | pandas |
| Visualization | Plotly |
| Machine Learning | scikit-learn |
| Frontend | HTML/CSS |
| Documentation | Markdown / Jekyll |
| Version Control | Git/GitHub |

---

# Project Structure

```text
soil-ml-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── CHANGELOG.md
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

Installation

Install dependencies:

pip install -r requirements.txt
Running the Application

Start the Flask development server:

python app.py

Open in browser:

http://127.0.0.1:5000
Machine Learning Workflow

The dashboard workflow includes:

Data loading
Risk classification
Dataset filtering
Feature selection
Train/test split
Model training
Prediction generation
Benchmark metric calculation
Interactive visualization
Documentation

The project includes Jekyll-ready documentation:

Usage Guide
Workflow Documentation
API Documentation
Architecture Overview
Developer Guide
FAIR Principles

Documentation files are located in:

docs/
Design Goals

The project prioritizes:

modularity
readability
maintainability
educational clarity
lightweight deployment
reusable workflows
Future Improvements

Potential future extensions:

PostgreSQL integration
geospatial analytics
satellite-data workflows
REST API endpoints
Docker deployment
dataset upload interface
model persistence
exportable reports
Changelog

See:

CHANGELOG.md
License

This repository is intended for educational and demonstration purposes.