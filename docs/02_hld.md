# High-Level Design (HLD)

## 1. System Overview

MediPredict AI is a unified machine learning application designed for preliminary risk prediction across four diseases:

- Diabetes
- Heart Disease
- Chronic Kidney Disease (CKD)
- Breast Cancer

The system separates data acquisition, preprocessing, model training, evaluation, prediction, backend services, and user-interface responsibilities.

## 2. High-Level Architecture

User
|
v
React Frontend
|
REST / HTTP
|
v
Flask API
|
+-------------------+
|                   |
v                   v
Validation     Predictor
|
v
Disease-specific ML Pipeline
|
v
Risk Prediction
|
v
API Response
|
v
React Frontend

## 3. Major Components

### Data Acquisition

Public datasets are acquired using an automated download script and stored locally for research experiments.

### Data Audit

The dataset audit verifies shape, columns, data types, missing values, suspicious values, duplicate rows and target distributions.

### Preprocessing

Disease-specific preprocessing handles missing values, invalid values, categorical encoding and numerical scaling.

### Machine Learning

Six classification algorithms are planned:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Support Vector Machine
5. K-Nearest Neighbours
6. XGBoost

### Evaluation

Each model will be evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

### Prediction

The selected model for each disease will be exposed through the prediction layer and Flask API.

### Frontend

A React-based interface is planned for disease selection, clinical parameter input, prediction results, model information, charts, voice support and safety messaging.

## 4. Data Flow

Public Dataset
|
v
Dataset Acquisition
|
v
Dataset Audit
|
v
Data Cleaning
|
v
Feature / Target Separation
|
v
Train / Test Split
|
v
Preprocessing Pipeline
|
v
Model Training
|
v
Model Evaluation
|
v
Best Model Selection
|
v
Model Artifact
|
v
Flask API
|
v
React UI
|
v
User Result

## 5. Deployment Architecture

User Browser / Mobile
|
v
React Frontend
|
v
Flask API
|
v
ML Model Artifacts

The intended deployment uses free-tier hosting where suitable for academic demonstration.

## 6. Security and Reliability

- Server-side input validation
- Safe model artifact handling
- No unnecessary personal health information storage
- Clear medical disclaimer
- Error handling
- Controlled model loading

## 7. Scalability

The modular architecture allows additional diseases, models and frontend features to be introduced without redesigning the entire system.

## 8. Safety

The system provides preliminary risk prediction and must not be represented as a confirmed medical diagnosis.
