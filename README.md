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
- Prediction Pipeline

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
- Other security-related features

The target column is `Result`.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- PyYAML
- Git
- GitHub

## ML Pipeline

```text
Dataset
   ↓
Data Ingestion
   ↓
Data Validation
   ↓
Data Transformation
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Trained Model
   ↓
Prediction

Project Structure
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
Model Performance

The trained model achieved:

Test Accuracy: 96.70%

The model was accepted during the model evaluation stage.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/skhumera0202/network-security-ml.git
cd network-security-ml
   
   2. Create a virtual environment
       
    python -m venv venv
 
   3. Activate the Virtual Environment

    For Windows PowerShell:
      venv\Scripts\activate

   4. Install Dependencies
       pip install -r requirements.txt

   5. Install the Project
      pip install -e .

   6. Run the Training Pipeline
      python -m networksecurity.pipeline.training
        
   7. Run the Prediction Pipeline
      python -m networksecurity.pipeline.prediction

   8. Run the Web Application
      python app.py

Then open the following URL in your browser:

http://127.0.0.1:5000


### 2. Which commands do **you** need to run?

**Right now: NONE of steps 2–5.** ✅

You already did them while building the project.

The commands are written in the README so that **someone cloning your GitHub project can follow them on their own computer**.

The only commands you would normally run when you want to use your existing project are:

```powershell
python -m networksecurity.pipeline.training
 
 or:

python -m networksecurity.pipeline.prediction

or, for the website:

python app.py

## Web Application

### Web Interface

![Network Security ML Web Interface](screenshots/web-interface.png)

### Prediction Result

![Prediction Result](screenshots/prediction-result.png)

## Tech Stack

- **Python**
- **Pandas** – Data processing
- **NumPy** – Numerical operations
- **Scikit-learn** – Machine learning
- **Random Forest Classifier** – Classification model
- **Flask** – Web application
- **PyYAML** – Configuration management
- **Joblib** – Model saving and loading
- **Git & GitHub** – Version control