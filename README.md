# AI-Based Multi-Disease Risk Prediction System

## Final Year Major Research Project

**MediPredict AI** is a unified machine learning-based system for preliminary risk prediction across multiple diseases using clinical parameters, comparative model evaluation, disease-specific preprocessing, and web-based deployment.

> **Important:** This system provides preliminary risk assessment for academic and research purposes. It is not a confirmed medical diagnosis and must not replace professional medical advice, diagnosis, or treatment.

---

## 1. Project Overview

Healthcare datasets contain different clinical parameters, data-quality challenges, and modelling requirements for different diseases. Many academic machine learning systems focus on a single disease or demonstrate only one predictive model.

This project proposes a unified platform supporting four disease-risk prediction tasks:

- Diabetes
- Heart Disease
- Chronic Kidney Disease (CKD)
- Breast Cancer

For each disease, multiple machine learning algorithms are evaluated using appropriate preprocessing and common performance metrics. The best-performing model is selected separately for each disease and integrated into the prediction workflow.

---

## 2. Research Gap

Existing machine learning-based healthcare prediction projects frequently focus on individual diseases or use a limited number of predictive algorithms.

This project addresses the identified gap by combining:

1. Multi-disease risk prediction
2. Comparative evaluation of multiple machine learning algorithms
3. Disease-specific preprocessing
4. Independent best-model selection
5. Reproducible training and evaluation
6. Web-based prediction workflow
7. Academic documentation and testing

The objective is to demonstrate a structured and reproducible machine learning workflow for preliminary disease-risk assessment rather than replacing clinical diagnosis.

---

## 3. Research Objectives

The major objectives of the project are:

- Develop a unified multi-disease machine learning system.
- Integrate datasets for four disease prediction tasks.
- Apply disease-appropriate preprocessing techniques.
- Compare multiple machine learning algorithms.
- Evaluate models using multiple performance metrics.
- Select the best-performing model independently for each disease.
- Build a web-based interface for user interaction.
- Provide preliminary risk predictions from clinical parameters.
- Maintain reproducible data, training, evaluation, and testing workflows.
- Document the complete research and software engineering process.

---

## 4. Diseases Covered

| Disease | Dataset | Prediction Task |
|---|---|---|
| Diabetes | Pima Indians Diabetes Dataset | Binary risk prediction |
| Heart Disease | UCI Heart Disease Dataset | Binary risk prediction |
| Chronic Kidney Disease | UCI Chronic Kidney Disease Dataset | Binary classification |
| Breast Cancer | UCI Breast Cancer Wisconsin Diagnostic Dataset | Benign/Malignant classification |

---

## 5. Machine Learning Models

| Model | Category | Purpose |
|---|---|---|
| Logistic Regression | Linear Classification | Interpretable baseline |
| Decision Tree | Tree-Based Classification | Rule-based modelling |
| Random Forest | Ensemble Learning | Robust non-linear modelling |
| Support Vector Machine | Kernel-Based Classification | Classification in feature space |
| K-Nearest Neighbours | Instance-Based Learning | Distance-based classification |
| XGBoost | Gradient Boosting | Advanced ensemble modelling |

The final model for each disease will be selected using actual experimental evaluation rather than predetermined assumptions.

---

## 6. Data Processing Methodology

The preprocessing pipeline is designed according to the characteristics of each dataset.

The workflow includes:

1. Dataset acquisition
2. Dataset validation
3. Data-quality auditing
4. Missing-value handling
5. Invalid-value handling
6. Categorical encoding
7. Feature scaling
8. Class-distribution analysis
9. Feature preparation
10. Train-test separation
11. Model training
12. Model evaluation

Disease-specific preprocessing is applied where required rather than forcing identical preprocessing rules across all datasets.

---

## 7. Model Evaluation

Models are evaluated using:

| Metric | Purpose |
|---|---|
| Accuracy | Overall classification correctness |
| Precision | Correctness of positive predictions |
| Recall | Ability to identify positive cases |
| F1-Score | Balance between precision and recall |
| ROC-AUC | Model discrimination capability |

### Experimental Results

Final performance values will be added only after actual model training and evaluation.

| Disease | Best Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---|---:|---:|---:|---:|---:|
| Diabetes | To be determined | TBD | TBD | TBD | TBD | TBD |
| Heart Disease | To be determined | TBD | TBD | TBD | TBD | TBD |
| CKD | To be determined | TBD | TBD | TBD | TBD | TBD |
| Breast Cancer | To be determined | TBD | TBD | TBD | TBD | TBD |

No placeholder value will be presented as a final experimental result.

---

## 8. System Architecture

The planned system follows a modular architecture:

User
|
v
Web Interface
|
v
Flask Backend / Prediction API
|
+-----------------------+
|                       |
v                       v
Input Validation     Disease Selection
|                       |
+-----------+-----------+
            |
            v
Disease-Specific Preprocessor
            |
            v
Selected Trained Model
            |
            v
Prediction + Risk Probability
            |
            v
Result Presentation

The machine learning workflow is separated from the web application to support reproducibility, testing, maintenance, and future model replacement.

---

## 9. Technology Stack

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib

### Backend

- Flask
- Python-based prediction services
- REST-style API design

### Frontend

- React
- Vite
- HTML
- CSS
- JavaScript

### Development

- Git
- GitHub
- Feature branches
- Pull requests
- Protected main branch

### Testing

- Pytest
- Unit testing
- Data preprocessing validation
- Model component validation
- Prediction workflow testing

---

# 10. Project Documentation

This table is the primary documentation checkout point for the complete project.

| No. | Document | Purpose | Checkout |
|---:|---|---|---|
| 01 | Literature Survey | Research papers, existing approaches, findings, and research gap | [Open](docs/01_literature_survey.md) |
| 02 | High-Level Design | System architecture, components, data flow, deployment, security, and scalability | [Open](docs/02_hld.md) |
| 03 | Low-Level Design | Modules, processing logic, prediction workflow, API planning, and error handling | [Open](docs/03_lld.md) |
| 04 | Dataset Documentation | Dataset sources, structure, targets, data quality, and governance | [Open](docs/04_dataset_documentation.md) |
| 05 | Preprocessing Methodology | Missing values, invalid values, encoding, scaling, leakage prevention, and reproducibility | [Open](docs/05_preprocessing_methodology.md) |
| 06 | Test Cases | Functional, prediction, validation, API, and UI test cases | [Open](docs/06_test_cases.md) |
| 07 | Initial UI Design | UI structure, user flow, prediction results, analytics, voice interaction, and responsiveness | [Open](docs/07_initial_ui_design.md) |
| 08 | Complexity, Cost, Social & Health | Complexity, cost, social relevance, and health considerations | [Open](docs/08_complexity_cost_social_health.md) |
| 09 | SDG, Legal & Environmental | SDG mapping, legal, cultural, environmental, and sustainability aspects | [Open](docs/09_sdg_legal_environmental.md) |
| 10 | Project Type | Academic classification, research orientation, technical domain, and scope | [Open](docs/10_project_type.md) |
| 11 | Monthly Project Progress Report | Monthly progress, accomplishments, assignments, plans, and guide assessment | [Open](docs/11_monthly_project_progress.md) |
| 12 | Review 2 Checklist | Complete Project Review 2 requirements and submission checklist | [Open](docs/12_review_2_checklist.md) |

---

## 11. Project Review 2 Coverage

| Review Requirement | Documentation |
|---|---|
| Literature Survey | [Open Literature Survey](docs/01_literature_survey.md) |
| High-Level Design | [Open HLD](docs/02_hld.md) |
| Low-Level Design | [Open LLD](docs/03_lld.md) |
| Dataset | [Open Dataset Documentation](docs/04_dataset_documentation.md) |
| Preprocessing | [Open Preprocessing Methodology](docs/05_preprocessing_methodology.md) |
| Test Cases | [Open Test Cases](docs/06_test_cases.md) |
| Initial UI Design | [Open Initial UI Design](docs/07_initial_ui_design.md) |
| Complexity / Cost / Social / Health | [Open Academic Evaluation](docs/08_complexity_cost_social_health.md) |
| Legal / Cultural / Environmental / SDG | [Open SDG / Legal / Environmental](docs/09_sdg_legal_environmental.md) |
| Project Type | [Open Project Type](docs/10_project_type.md) |
| Monthly Project Progress | [Open MPR Documentation](docs/11_monthly_project_progress.md) |
| Review 2 Checklist | [Open Review 2 Checklist](docs/12_review_2_checklist.md) |

---

## 12. Current Project Status

### Engineering Foundation

- Project repository established
- Git workflow established
- Protected main branch
- Modular source structure
- Dataset acquisition workflow
- Dataset audit workflow
- Preprocessing foundation
- Model factory
- Prediction component
- Unit tests
- Review 2 documentation foundation

### Validation

Current baseline test suite:

12 tests passed

Final machine learning performance will be added after the complete training and evaluation pipeline has been executed.

---

## 13. Repository Structure

ai-multidisease-prediction/
|
+-- app/
|   +-- app.py
|   +-- static/
|   +-- templates/
|
+-- data/
|   +-- raw/
|   +-- processed/
|
+-- models/
|   +-- diabetes/
|   +-- heart/
|   +-- ckd/
|   +-- breast_cancer/
|
+-- reports/
|   +-- results/
|
+-- src/
|   +-- data/
|   +-- models/
|   +-- prediction/
|   +-- training/
|   +-- config.py
|
+-- tests/
|
+-- docs/
|
+-- requirements.txt
+-- LICENSE
+-- README.md

---

## 14. Reproducibility and Research Integrity

The project follows a reproducible machine learning workflow.

Key principles include:

- Fixed random state where applicable.
- Dataset auditing before modelling.
- Disease-specific preprocessing.
- Separation of training and evaluation workflows.
- Prevention of data leakage through appropriate pipeline design.
- Actual experimental results only.
- Version-controlled source code.
- Testable software components.
- Documentation of assumptions and limitations.

---

## 15. Limitations

The project has the following limitations:

- Prediction quality depends on dataset quality and representativeness.
- Public datasets may not represent all real-world patient populations.
- Different diseases require different clinical parameters.
- Dataset size may limit generalisation.
- The system has not undergone clinical validation.
- Predictions are not confirmed medical diagnoses.
- Real-world healthcare deployment would require appropriate regulatory, security, privacy, and clinical validation processes.

---

## 16. Future Scope

Potential future improvements include:

- Hyperparameter optimization
- Larger and more diverse datasets
- Explainable AI using SHAP or LIME
- Advanced ensemble techniques
- Deep learning models
- Cloud deployment
- Electronic Health Record integration
- IoT and wearable-device integration
- Continuous model monitoring
- Clinical validation
- Privacy-preserving healthcare AI

---

## 17. Social, Health and Sustainability Relevance

The project demonstrates the application of machine learning to healthcare-related risk assessment in an academic research setting.

The system incorporates responsible-use considerations by clearly communicating that its predictions are preliminary and should not be treated as medical diagnoses.

The project aligns particularly with:

- SDG 3: Good Health and Well-Being
- SDG 9: Industry, Innovation and Infrastructure

Detailed discussion is available in the corresponding project documentation.

---

## 18. Team

| Team Member | Roll Number |
|---|---:|
| Karan Kumar Tiwari | 2302220100093 |
| Payal Chauhan | 2302220100125 |
| Mamta Tiwari | 2302220100099 |
| Devesh Chauhan | 2302220100064 |

**Guide:** Mr. Anurag Gupta, Assistant Professor, Department of Computer Science

**College:** ITS Engineering College, Greater Noida

**University:** Dr. A.P.J. Abdul Kalam Technical University, Lucknow, Uttar Pradesh

---

## 19. License

This project is released under the MIT License.

See [LICENSE](LICENSE) for details.

---

## 20. Academic Disclaimer

This repository is developed as a final-year major research project.

The system is intended for academic and research demonstration only. It provides preliminary machine learning-based risk assessment and must not be interpreted as a clinically validated diagnostic system.

Final conclusions and performance claims will be based on documented experimental results.
