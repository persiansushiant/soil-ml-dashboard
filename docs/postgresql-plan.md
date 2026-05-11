# PostgreSQL Integration Plan

## Overview

The current prototype uses CSV-based datasets for simplicity and rapid prototyping.

However, the project architecture is intentionally designed so that the data layer can later be replaced with PostgreSQL-based workflows.

---

## Motivation

A PostgreSQL integration would improve:

- scalability
- data management
- multi-user workflows
- centralized storage
- reproducibility
- metadata management

This aligns with larger environmental-data workflows and research infrastructure needs.

---

## Current Data Workflow

The current prototype loads data from:

```text
data/soil_data.csv
```

using pandas-based workflows.

---

## Planned Database Workflow

Future architecture:

```text
User Request
    ↓
Flask Application
    ↓
Data Utility Layer
    ↓
PostgreSQL Database
    ↓
Processed Dataset
    ↓
Visualization / ML Workflow
```

---

## Proposed Database Tables

Potential database structure:

### soil_samples

Stores:

- sample identifiers
- timestamps
- geographic coordinates
- soil types
- collection metadata

---

### environmental_measurements

Stores:

- soil moisture
- temperature
- pH
- organic carbon
- nitrogen
- spectral measurements

---

### satellite_features

Stores:

- remote sensing features
- vegetation indices
- satellite-derived variables
- Ecodatacube integrations

---

### benchmark_results

Stores:

- trained-model outputs
- benchmark metrics
- model metadata
- experiment history

---

## Python Integration Plan

Potential Python libraries:

- psycopg2
- SQLAlchemy
- pandas SQL workflows

---

## Planned Features

Future PostgreSQL integration may support:

- live querying
- dynamic filtering
- larger datasets
- user-uploaded observations
- versioned datasets
- metadata tracking
- experiment logging

---

## FAIR Alignment

Database-backed workflows can improve FAIR compliance by supporting:

- structured metadata
- reproducible querying
- centralized storage
- standardized access patterns

---

## Future Infrastructure Possibilities

Potential future deployment options:

- Dockerized PostgreSQL
- cloud-hosted databases
- REST API integration
- asynchronous processing
- distributed analytics workflows

---

## Design Philosophy

The current prototype intentionally separates:

- data access
- machine learning
- visualization

This modular structure simplifies future migration from CSV-based workflows to PostgreSQL-based infrastructure.