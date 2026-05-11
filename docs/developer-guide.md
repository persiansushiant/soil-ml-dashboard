# Developer Guide

## Overview

This document describes the development workflow and project organization for the Soil ML Dashboard.

The goal of the project structure is to keep the application:

- modular
- readable
- maintainable
- easy to extend

---

## Local Development

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

---

## Development Workflow

Typical workflow:

1. create or modify utility modules
2. test dashboard locally
3. verify charts and ML workflows
4. commit changes using Git
5. update documentation if needed

---

## Utility Modules

### data_utils.py

Responsible for:

- dataset loading
- filtering
- feature engineering
- risk classification

---

### ml_utils.py

Responsible for:

- model creation
- training
- benchmarking
- metric calculation

---

### chart_utils.py

Responsible for:

- Plotly chart generation
- reusable visualization functions

---

## Styling

Frontend styles are separated into:

```text
static/css/style.css
```

This improves frontend maintainability and readability.

---

## Documentation Workflow

Documentation is stored in:

```text
docs/
```

The project is structured for:

- Jekyll
- GitHub Pages
- self-study material
- lightweight technical documentation

---

## Git Workflow

Example workflow:

```bash
git status
git add .
git commit -m "Add feature description"
```

---

## Code Style Goals

The project aims to prioritize:

- small reusable functions
- descriptive naming
- separated responsibilities
- lightweight architecture
- readable workflows

---

## Potential Improvements

Future development possibilities:

- PostgreSQL integration
- API expansion
- dataset upload workflows
- Docker deployment
- authentication
- geospatial analytics
- satellite-data integration
- model persistence