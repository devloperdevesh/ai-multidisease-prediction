# MediPredict AI

### AI-Based Medical Diagnosis System Using Machine Learning for Multi-Disease Prediction

**Final Year Project | Computer Science & Engineering**
ITS Engineering College, Greater Noida
Dr. A.P.J. Abdul Kalam Technical University, Lucknow

[Live Demo](https://medipredict-ai-two.vercel.app/) · [Backend API](https://medipredict-ai-api.onrender.com/api/health) · [GitHub Repository](https://github.com/devloperdevesh/ai-multidisease-prediction)

**4 Disease Categories · 6 Algorithms · 24 Model Experiments**

---

## 1. Project Overview

MediPredict AI is an academic machine-learning research prototype that brings four disease-specific prediction workflows into one web application.

The project explores how structured benchmark datasets and machine-learning classification models can be used for preliminary risk classification.

### Diseases covered

- Diabetes
- Heart Disease
- Chronic Kidney Disease (CKD)
- Breast Cancer

The platform is intended for academic research and demonstration. It does not provide a confirmed medical diagnosis.

## 2. Research Gap

Many existing academic systems focus on a single disease. This project explores a unified approach that combines multiple disease-specific models, model comparison, evaluation evidence and web application integration.

## 3. Objectives

- Prepare and inspect public benchmark datasets.
- Develop four disease-specific prediction workflows.
- Train and compare six classification algorithms per disease.
- Evaluate models using test metrics and cross-validation.
- Integrate selected models with a web application.
- Document reproducible experiment results and limitations.

## 4. Dataset Inventory

| Disease | Dataset | Records | Features |
|---|---|---:|---:|
| Diabetes | Pima Indians Diabetes | 768 | 8 |
| Heart Disease | Cleveland Heart Disease | 303 | 13 |
| CKD | UCI Chronic Kidney Disease | 400 | 24 |
| Breast Cancer | Wisconsin Diagnostic | 569 | 30 |

These are public benchmark datasets, not live hospital records or a representative sample of all patient populations.

## 5. Algorithms

Each disease was evaluated with six algorithms:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Support Vector Machine (SVM)
5. K-Nearest Neighbors (KNN)
6. XGBoost

**Total: 4 diseases × 6 algorithms = 24 experiment records.**

## 6. Selected Model Results

The following values are read from eports/results/best_models.json.

| Disease | Selected Model | Accuracy | Precision | Recall | F1-score | Test ROC-AUC | CV ROC-AUC |
|---|---|---:|---:|---:|---:|---:|---:|
| Diabetes | logistic_regression | 70.78% | 60.00% | 50.00% | 54.55% | 0.8130 | 0.8434 |
| Heart Disease | logistic_regression | 86.89% | 81.25% | 92.86% | 86.67% | 0.9665 | 0.8968 |
| Chronic Kidney Disease | logistic_regression | 100.00% | 100.00% | 100.00% | 100.00% | 1.0000 | 1.0000 |
| Breast Cancer | logistic_regression | 96.49% | 97.50% | 92.86% | 95.12% | 0.9960 | 0.9958 |

These are reported experiment results, not independent clinical validation results. The unusually high CKD metrics require additional investigation for data leakage, duplicate records and generalization.

See [complete evaluation evidence](docs/MODEL_EVALUATION_EVIDENCE.md) for the full experiment inventory.

## 7. Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Cross-validation ROC-AUC
- Confusion matrix

## 8. System Workflow

1. Public dataset collection and inspection
2. Data cleaning and preprocessing
3. Disease-specific feature preparation
4. Model training
5. Cross-validation and test-set evaluation
6. Model comparison and selection
7. Model persistence
8. API integration
9. Frontend input and result presentation

## 9. Technology Stack

| Layer | Technologies |
|---|---|
| Programming | Python, JavaScript |
| Frontend | React, Vite, HTML, CSS |
| Backend | Flask, REST API |
| Machine Learning | Scikit-learn, XGBoost |
| Data Processing | Pandas, NumPy |
| Model Persistence | Joblib |
| Testing | Pytest |
| Deployment | Vercel, Render |
| Version Control | Git, GitHub |

## 10. Application Components

**Frontend**
- Disease selection and input forms
- Prediction result components
- Research and analytics views
- Workspace and login components
- API service layer

**Backend**
- Dataset processing
- Model training pipeline
- Prediction schemas and predictor
- Flask API and report storage

Source-code components alone do not establish successful end-to-end integration. Refer to the verification report for tested runtime claims.

## 11. Testing

A previous reported backend test run completed with **41 passed in 2.90 seconds**. Re-run the commands below to verify the current merged branch.

## 12. Project Team

| Team Member | Role |
|---|---|
| Devesh Chauhan | Technical Lead |
| Karan Kumar Tiwari | UI / Frontend Developer |
| Payal Chauhan | Research & Presentation |
| Mamta Tiwari | Research & Documentation |

**Project Guide:** Mr. Anurag Gupta, Assistant Professor, Department of Computer Science.

## 13. Documentation and Research Evidence

| Resource | Description |
|---|---|
| [Project Report](docs/PROJECT_REPORT.md) | Academic project report |
| [Implementation Status](docs/IMPLEMENTATION_STATUS.md) | Verification and implementation status |
| [Model Evaluation Evidence](docs/MODEL_EVALUATION_EVIDENCE.md) | Detailed experiment results |
| [High-Level Design](docs/02_hld.md) | System architecture |
| [Low-Level Design](docs/03_lld.md) | Component design |
| [Dataset Documentation](docs/04_dataset_documentation.md) | Dataset details |
| [Preprocessing Methodology](docs/05_preprocessing_methodology.md) | Data preparation |
| [Literature Survey](docs/01_literature_survey.md) | Related work |
| [Test Cases](docs/06_test_cases.md) | Test documentation |
| [Screenshots](docs/SCREENSHOTS.md) | Application screenshots |

## 14. Local Setup

### Clone the repository

`ash
git clone https://github.com/devloperdevesh/ai-multidisease-prediction.git
cd ai-multidisease-prediction
`

### Python environment

`powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
`

### Run the backend

`powershell
python -m app.api.server
`

### Run the frontend in another terminal

`powershell
npm --prefix frontend install
npm --prefix frontend run dev
`

### Run backend tests

`powershell
python -m pytest -q
`

### Build frontend

`powershell
npm --prefix frontend run build
`

### Reproduce model experiments

`powershell
python -m src.training.train_all
`

Re-training can overwrite model artifacts and regenerate results. Preserve a backup before running it.

## 15. Research Limitations and Responsible Use

- Public benchmark datasets may not represent all patient populations.
- Model scores depend on data quality, splitting and preprocessing.
- CKD's unusually high scores require leakage and duplicate-record investigation.
- Independent external clinical validation has not been established.
- The application is not clinically approved.
- Predictions must not be used for treatment decisions.

## 16. Future Scope

- Independent external dataset validation
- Explainable AI using SHAP or LIME
- Model calibration and threshold analysis
- Dataset provenance and leakage investigation
- Model monitoring and drift detection
- Secure assessment storage
- Clinical collaboration and validation

## 17. Sustainable Development Goals

- SDG 3: Good Health and Well-being
- SDG 9: Industry, Innovation and Infrastructure

## 18. License

Released under the [MIT License](LICENSE).

---

**Disclaimer:** MediPredict AI is an academic research prototype. It is not a substitute for a qualified medical professional, laboratory testing, diagnosis or treatment.
