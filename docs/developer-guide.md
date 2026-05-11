# Developer Guide

## Overview

This document describes the development workflow and project organization for the Soil ML Dashboard.

The goal of the project structure is to keep the application:

- modular
- readable
- maintainable
- easy to extend

---

# Local Development

## Install Dependencies

```bash
pip install -r requirements.txt

Run the Application
python app.py

Open in browser:

http://127.0.0.1:5000
Development Workflow

Typical workflow:

Create or modify utility modules
Test dashboard functionality locally
Verify charts and ML workflows
Commit changes using Git
Update documentation if needed
Utility Modules
data_utils.py

Responsible for:

dataset loading
filtering
feature engineering
risk classification
ml_utils.py

Responsible for:

model creation
training
benchmarking
metric calculation
chart_utils.py

Responsible for:

Plotly chart generation
reusable visualization functions
Styling

Frontend styles are separated into:

static/css/style.css

This improves frontend maintainability and readability.

Documentation Workflow

Documentation is stored in:

docs/

The project is structured for:

Jekyll
GitHub Pages
self-study material
lightweight technical documentation
Git Workflow

Example commit workflow:

git status
git add .
git commit -m "Add feature description"
Code Style Goals

The project aims to prioritize:

small reusable functions
descriptive naming
separated responsibilities
lightweight architecture
readable workflows
Potential Improvements

Future development possibilities:

PostgreSQL integration
API expansion
dataset upload workflows
Docker deployment
authentication
geospatial analytics
satellite-data integration
model persistence

---

# حالا `docs/_config.yml` را کامل جایگزین کن

```yml
title: Soil ML Dashboard Documentation
description: Documentation for a Flask-based soil health machine learning dashboard

theme: minima

header_pages:
  - usage.md
  - workflow.md
  - model-benchmarking.md
  - fair-principles.md
  - architecture.md
  - api.md
  - developer-guide.md