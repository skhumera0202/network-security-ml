# Network Security ML

A Machine Learning project for detecting phishing websites using URL and website-related security features.

## Project Overview

This project implements an end-to-end Machine Learning pipeline for phishing website detection.

The pipeline includes:

- Data Ingestion
- Data Validation
- Data Transformation
- Model Training
- Model Evaluation
- Training Pipeline

The project is structured as a modular Python package so that each stage of the ML workflow can be developed and tested separately.

## Dataset

The dataset contains features related to URLs and website characteristics, including:

- IP address usage
- URL length
- URL shortening services
- HTTPS
- SSL state
- Subdomains
- Website traffic
- Page rank
- Google indexing
- DNS records
- And other security-related features

The target column is:

`Result`

## Project Structure

```text
network-security-ml/
│
├── data/
│   └── phisingData.csv
│
├── data_schema/
│   └── schema.yaml
│
├── src/
│   └── networksecurity/
│       ├── cloud/
│       ├── components/
│       │   ├── data_ingestion.py
│       │   ├── data_validation.py
│       │   ├── data_transformation.py
│       │   ├── model_trainer.py
│       │   └── model_evaluation.py
│       │
│       ├── constant/
│       ├── entity/
│       ├── exception/
│       ├── logging/
│       └── pipeline/
│           ├── training.py
│           └── prediction.py
│
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md