<div align="center">

# MediPredict AI

### AI-Based Medical Diagnosis System Using Machine Learning for Multi-Disease Prediction

**Final Year Major Project | Computer Science & Engineering**

ITS Engineering College, Greater Noida
Dr. A.P.J. Abdul Kalam Technical University, Lucknow

[![Python](https://img.shields.io/badge/Python-ML%20Backend-blue?logo=python)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)](https://react.dev/)
[![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange?logo=scikitlearn)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[**Live Demo**](https://medipredict-ai-two.vercel.app/) ·
[**Backend API**](https://medipredict-ai-api.onrender.com/api/health) ·
[**GitHub Repository**](https://github.com/devloperdevesh/ai-multidisease-prediction)

**4 Disease Categories** · **6 ML Algorithms** · **24 Model Experiments**

</div>

---

## 1. Project Overview

**MediPredict AI** is an academic machine-learning research prototype that brings four disease-specific prediction workflows into one web application.

The project explores how structured public benchmark datasets and machine-learning classification algorithms can be used for preliminary risk classification, comparative model evaluation and web-based result presentation.

### Diseases Covered

| Disease | Prediction Workflow |
|:---|:---|
| Diabetes | Diabetes risk classification |
| Heart Disease | Heart disease risk classification |
| Chronic Kidney Disease (CKD) | CKD risk classification |
| Breast Cancer | Breast cancer classification |

> **Research scope:** MediPredict AI is an academic prototype, not a clinically approved diagnostic system. Its predictions are experimental and must not replace professional medical advice.

## 2. Research Gap

Many existing academic machine-learning projects focus on a single disease. There is an opportunity to explore unified systems that combine multiple disease-specific prediction workflows, comparative model evaluation and web application integration.

MediPredict AI explores this opportunity through four independent prediction workflows integrated into a common application.

## 3. Project Objectives

- Collect, inspect and preprocess public benchmark datasets.
- Develop four disease-specific machine-learning workflows.
- Train and compare six classification algorithms for each disease.
- Evaluate model performance using classification metrics.
- Apply cross-validation to examine model performance across data partitions.
- Select and persist models for application integration.
- Develop a web interface for prediction input and result presentation.
- Document experiments, implementation evidence and research limitations.

## 4. Dataset Inventory

| Disease | Dataset | Records | Features |
|:---|:---|---:|---:|
| Diabetes | Pima Indians Diabetes | 768 | 8 |
| Heart Disease | Cleveland Heart Disease | 303 | 13 |
| CKD | UCI Chronic Kidney Disease | 400 | 24 |
| Breast Cancer | Wisconsin Diagnostic | 569 | 30 |
| **Total** | **4 datasets** | **2,040** | — |

These are public benchmark datasets, not live hospital records or a representative sample of all patient populations.

*Feature counts describe the reported dataset inventory and may differ from the final features retained after preprocessing.*

## 5. Machine Learning Algorithms

Six classification algorithms were evaluated for each disease.

| No. | Algorithm | Learning Approach |
|:---:|:---|:---|
| 1 | Logistic Regression | Linear Classification |
| 2 | Decision Tree | Tree-Based Learning |
| 3 | Random Forest | Ensemble Learning |
| 4 | Support Vector Machine (SVM) | Kernel-Based Learning |
| 5 | K-Nearest Neighbors (KNN) | Instance-Based Learning |
| 6 | XGBoost | Gradient Boosting |

<div align="center">

**4 Diseases × 6 Algorithms = 24 Model Experiments**

</div>

## 6. Selected Model Performance

The following results are reported from `reports/results/best_models.json`.

| Disease | Selected Model | Accuracy | Precision | Recall | F1-score | Test ROC-AUC | CV ROC-AUC |
|:---|:---|---:|---:|---:|---:|---:|---:|
| Diabetes | Logistic Regression | 70.78% | 60.00% | 50.00% | 54.55% | 0.8130 | 0.8434 |
| Heart Disease | Logistic Regression | 86.89% | 81.25% | 92.86% | 86.67% | 0.9665 | 0.8968 |
| CKD | Logistic Regression | 100.00% | 100.00% | 100.00% | 100.00% | 1.0000 | 1.0000 |
| Breast Cancer | Logistic Regression | 96.49% | 97.50% | 92.86% | 95.12% | 0.9960 | 0.9958 |

**Important research interpretation**

- These are reported experimental results from the current project artifacts.
- Test ROC-AUC and cross-validation ROC-AUC are separate evaluation results.
- The unusually high CKD metrics require further investigation into possible data leakage, duplicate records, preprocessing and generalization.
- Independent external clinical validation has not been established.

See [Model Evaluation Evidence](docs/MODEL_EVALUATION_EVIDENCE.md) for the detailed experiment inventory.

## 7. Evaluation Metrics

| Metric | Purpose |
|:---|:---|
| Accuracy | Proportion of correct predictions |
| Precision | Correctness of positive predictions |
| Recall | Identification of actual positive cases |
| F1-score | Harmonic balance of precision and recall |
| ROC-AUC | Discrimination across classification thresholds |
| Cross-validation ROC-AUC | Performance across validation folds |
| Confusion Matrix | Summary of correct and incorrect classifications |

## 8. System Workflow

<div align="center">

**Dataset Collection & Inspection**
↓
**Data Cleaning & Preprocessing**
↓
**Disease-Specific Feature Preparation**
↓
**Model Training**
↓
**Cross-Validation & Test Evaluation**
↓
**Model Comparison & Selection**
↓
**Model Persistence**
↓
**Backend API Integration**
↓
**Frontend Prediction Interface**
↓
**Result Presentation**

</div>

## 9. Technology Stack

| Layer | Technologies |
|:---|:---|
| Programming Languages | Python, JavaScript |
| Frontend | React, Vite, HTML, CSS |
| Backend | Flask, REST API |
| Machine Learning | Scikit-learn, XGBoost |
| Data Processing | Pandas, NumPy |
| Model Persistence | Joblib |
| Testing | Pytest |
| Deployment | Vercel, Render |
| Version Control | Git, GitHub |

## 10. Application Components

### Frontend

- Disease selection interface
- Disease-specific input forms
- Prediction result components
- Research and analytics views
- Workspace and login components
- API service layer

### Backend

- Dataset processing and preprocessing
- Model training pipeline
- Disease-specific prediction workflows
- Prediction schemas and predictor components
- Flask REST API
- Report storage and result handling

*The presence of source-code components alone does not establish successful end-to-end integration. Refer to implementation and verification documentation for tested runtime claims.*

## 11. Testing and Verification

The project includes backend testing using Pytest and frontend production-build verification.

A previously reported backend test run completed with 41 passing tests. This is a historical result, not a fresh verification of every current branch revision.

Run the following commands to verify the current code:

```powershell
python -m pytest -q
npm.cmd --prefix frontend run build
```

## 12. Project Team

| Team Member | Responsibility |
|:---|:---|
| Devesh Chauhan | Technical Lead |
| Karan Kumar Tiwari | UI / Frontend Development |
| Payal Chauhan | Research & Presentation |
| Mamta Tiwari | Research & Documentation |

**Project Guide:** Mr. Anurag Gupta, Assistant Professor, Department of Computer Science.

## 13. Documentation and Research Resources

| Resource | Description |
|:---|:---|
| [Project Report](docs/PROJECT_REPORT.md) | Academic project report |
| [Implementation Status](docs/IMPLEMENTATION_STATUS.md) | Implementation and verification status |
| [Model Evaluation Evidence](docs/MODEL_EVALUATION_EVIDENCE.md) | Detailed model experiment results |
| [High-Level Design](docs/02_hld.md) | System architecture |
| [Low-Level Design](docs/03_lld.md) | Component-level design |
| [Dataset Documentation](docs/04_dataset_documentation.md) | Dataset information |
| [Preprocessing Methodology](docs/05_preprocessing_methodology.md) | Data preparation |
| [Literature Survey](docs/01_literature_survey.md) | Related research |
| [Test Cases](docs/06_test_cases.md) | Testing documentation |
| [Screenshots](docs/SCREENSHOTS.md) | Application screenshots |

## 14. Local Installation and Setup

### Prerequisites

- Python
- Node.js and npm
- Git

### Clone the Repository

```powershell
git clone https://github.com/devloperdevesh/ai-multidisease-prediction.git
cd ai-multidisease-prediction
```

### Create a Python Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Start the Backend

```powershell
python -m app.api.server
```

### Install and Start the Frontend

Open another terminal:

```powershell
npm.cmd --prefix frontend install
npm.cmd --prefix frontend run dev
```

### Run Backend Tests

```powershell
python -m pytest -q
```

### Build the Frontend

```powershell
npm.cmd --prefix frontend run build
```

### Reproduce Model Experiments

```powershell
python -m src.training.train_all
```

> **Reproducibility warning:** Training may overwrite model artifacts or regenerate experiment results. Preserve existing research outputs before retraining.

## 15. Research Limitations and Responsible Use

1. Public benchmark datasets may not represent all patient populations.
2. Model scores depend on data quality, splitting and preprocessing.
3. CKD's unusually high scores require investigation into leakage and duplicate records.
4. Independent external clinical validation has not been established.
5. The application has not been established as clinically approved.
6. Predictions must not be used independently for diagnosis or treatment decisions.

## 16. Future Scope

- Independent external dataset validation
- Explainable AI using SHAP or LIME
- Model calibration and threshold analysis
- Dataset provenance and leakage investigation
- Model monitoring and data-drift detection
- Secure prediction history and assessment storage
- Improved usability and accessibility
- Collaboration with qualified clinical researchers

## 17. Sustainable Development Goals

| SDG | Goal | Project Relevance |
|:---:|:---|:---|
| SDG 3 | Good Health and Well-being | Academic exploration of disease-risk prediction |
| SDG 9 | Industry, Innovation and Infrastructure | Application of machine learning and software engineering |

## 18. License

Released under the [MIT License](LICENSE).

---

<div align="center">

### MediPredict AI

**An Academic Exploration of Machine Learning for Multi-Disease Prediction**

Final Year Major Project
Department of Computer Science & Engineering
ITS Engineering College, Greater Noida

[GitHub Repository](https://github.com/devloperdevesh/ai-multidisease-prediction) · [Live Demo](https://medipredict-ai-two.vercel.app/)

</div>

**Disclaimer:** MediPredict AI is an academic research prototype. It is not a substitute for a qualified medical professional, laboratory testing, diagnosis or treatment. All predictions are experimental and must not be used as the sole basis for healthcare decisions.
