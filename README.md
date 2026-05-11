# Soil ML Dashboard

A Flask-based interactive dashboard for exploring soil health data, applying filters, visualizing environmental indicators, and benchmarking simple machine learning regression models.

This project was created as a compact research-tool prototype inspired by soil health monitoring workflows.

## Features

- Interactive Flask dashboard
- Soil data filtering by country and soil type
- Data processing with pandas
- Interactive charts with Plotly
- Soil risk classification based on moisture
- Machine learning regression benchmark
- Model comparison using MAE, RMSE, and R²
- Clean modular Python structure
- Prepared documentation folder for Jekyll/GitHub Pages

## Tech Stack

- Python
- Flask
- pandas
- Plotly
- scikit-learn
- HTML/CSS
- Git/GitHub

## Project Structure

```text
soil-ml-dashboard/
│
├── app.py
├── requirements.txt
├── README.md
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

Open the dashboard in the browser:
http://127.0.0.1:5000

Dashboard Workflow

The dashboard allows the user to:

Filter soil data
Explore environmental indicators
Select a machine learning target variable
Choose a regression model
Benchmark model performance
Compare multiple models
Machine Learning Pipeline

The machine learning workflow includes:

Load soil data from CSV
Create derived risk-level features
Apply dataset filters
Select numeric feature columns
Split the dataset into train/test sets
Train a regression model
Generate predictions
Calculate evaluation metrics
Visualize actual vs predicted values
Compare model performance
Supported Models
Linear Regression
Decision Tree Regressor
Random Forest Regressor
Evaluation Metrics
Metric	Description
MAE	Mean Absolute Error
RMSE	Root Mean Squared Error
R²	Explained variance / goodness of fit
Dashboard Components
Environmental Visualizations
Temperature vs moisture scatter plot
Average moisture by country
Organic carbon histogram
Soil risk-level analysis
Machine Learning Components
Model benchmark dashboard
Actual vs predicted visualization
Multi-model comparison
Performance metrics table
Data Processing

The dashboard uses pandas for:

Data loading
Filtering
Feature engineering
Aggregation
Statistical summaries
Modular Project Design

The application separates responsibilities into utility modules:

data_utils.py

Handles:

CSV loading
Risk classification
Dataset filtering
Filter-option generation
ml_utils.py

Handles:

Model creation
Training workflows
Metric calculations
Benchmark comparison
chart_utils.py

Handles:

Plotly chart creation
Dashboard visualizations
Reusable plotting functions
Documentation Goal

The project structure is prepared for:

Jekyll documentation
GitHub Pages publishing
Self-study tutorials
Research workflow explanations

Planned documentation pages:

Usage guide
Data workflow
Benchmarking workflow
FAIR principles
Future improvements
Future Improvements
CSV upload support
PostgreSQL integration
Additional regression models
Cross-validation workflows
Exportable benchmark reports
REST API expansion
Field-data collection interface
Satellite data integration
Interactive geospatial visualization
Development Notes

This project was designed as a lightweight demonstration of:

Environmental data analysis
Scientific dashboard design
Machine learning benchmarking
Research-tool prototyping
Modular Python development
Interactive visualization workflows
License

This repository is intended for educational and demonstration purposes.