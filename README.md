# AI-Based Multi-Disease Risk Prediction System

## Final Year Major Research Project

A unified machine learning system for preliminary risk prediction of multiple diseases using clinical parameters, comparative model evaluation, and web-based deployment.

## Overview

This project develops a unified AI/ML platform for preliminary risk prediction of:

- Diabetes
- Heart Disease
- Chronic Kidney Disease (CKD)
- Breast Cancer

For each disease, multiple machine learning models are trained, evaluated, compared, and the best-performing model is selected for deployment.

> This system provides preliminary risk assessment and is not a confirmed medical diagnosis.

## Research Gap

Many existing systems focus on a single disease. There are fewer unified systems that combine **multiple disease prediction, model comparison, and web deployment**.

This project addresses this gap through a single platform supporting four disease prediction tasks with consistent model evaluation and deployment.

## Objectives

- Build a unified multi-disease prediction system.
- Compare multiple machine learning algorithms.
- Apply appropriate preprocessing to each dataset.
- Evaluate models using multiple performance metrics.
- Select the best-performing model for each disease.
- Deploy the selected models through a web application.

## Diseases Covered

| Disease | Dataset |
|---|---|
| Diabetes | Pima Indians Diabetes Dataset |
| Heart Disease | Cleveland / Statlog Heart Disease Dataset |
| CKD | UCI Chronic Kidney Disease Dataset |
| Breast Cancer | Publicly available Breast Cancer dataset |

## Machine Learning Models

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- K-Nearest Neighbours (KNN)
- XGBoost

## Data Processing

The datasets are prepared using appropriate techniques such as:

- Missing value handling
- Exploratory Data Analysis (EDA)
- Categorical encoding
- Feature scaling
- Class-imbalance handling
- Feature selection

## Model Evaluation

Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

The best-performing model is selected separately for each disease.

## Prediction

Users provide disease-specific clinical parameters through the web application. The selected model processes the input and generates a preliminary disease-risk prediction.

## Technology Stack

**Machine Learning:** Python, Pandas, NumPy, Scikit-learn, XGBoost

**Web:** Flask / Streamlit, HTML, CSS, Bootstrap, JavaScript

**Development:** Git, GitHub

## Results

Final experimental results will be added after completing model training and evaluation.

| Disease | Best Model | Accuracy | F1-Score | ROC-AUC |
|---|---|---:|---:|---:|
| Diabetes | TBD | TBD | TBD | TBD |
| Heart Disease | TBD | TBD | TBD | TBD |
| CKD | TBD | TBD | TBD | TBD |
| Breast Cancer | TBD | TBD | TBD | TBD |

## Research Contribution

- Unified prediction of four diseases
- Comparative evaluation of six ML algorithms
- Disease-specific preprocessing
- Best-model selection
- Web-based risk prediction
- Reproducible machine learning workflow

## Limitations

- Performance depends on dataset quality and size.
- Different diseases require different clinical parameters.
- Predictions are not confirmed medical diagnoses.
- Real-world clinical validation is required before practical healthcare deployment.

## Future Scope

- Hyperparameter optimization
- Larger and more diverse datasets
- Explainable AI
- Deep learning
- Cloud deployment
- EHR integration
- Real-world clinical validation

## Team

| Name | Roll Number |
|---|---:|
| Karan Kumar Tiwari | 2302220100093 |
| Payal Chauhan | 2302220100125 |
| Mamta Tiwari | 2302220100099 |
| Devesh Chauhan | 2302220100064 |

**Guide:** Mr. Anurag Gupta, Assistant Professor, Department of Computer Science  
**College:** ITS Engineering College, Greater Noida  
**University:** Dr. A.P.J. Abdul Kalam Technical University, Lucknow, Uttar Pradesh

## Disclaimer

This project is developed for academic and research purposes. It should not be used as a replacement for professional medical diagnosis or treatment.

## License

MIT License
