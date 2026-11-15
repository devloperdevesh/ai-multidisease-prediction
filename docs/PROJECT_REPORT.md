# MediPredict AI — Final Year Project Report

## Project information

**Project title:** AI-Based Medical Diagnosis System Using Machine Learning for Multi-Disease Prediction

**Institution:** ITS Engineering College, Greater Noida
**University:** Dr. A.P.J. Abdul Kalam Technical University, Lucknow
**Department:** Computer Science and Engineering
**Project guide:** Mr. Anurag Gupta, Assistant Professor (CSE)

### Project team

| Student | Roll number |
|---|---|
| Karan Kumar Tiwari | 2302220100093 |
| Payal Chauhan | 2302220100125 |
| Mamta Tiwari | 2302220100099 |
| Devesh Chauhan | 2302220100064 |

## Abstract

MediPredict AI is an academic machine-learning project that brings four disease-specific prediction workflows into one web application. The project evaluates models for Diabetes, Heart Disease, Chronic Kidney Disease and Breast Cancer using public benchmark datasets. Its research workflow includes dataset preparation, model training, metric-based comparison, model selection and integration with a web interface.

The repository contains 24 recorded model experiments, corresponding to six algorithms for each of the four disease categories. The project is intended for preliminary academic risk-prediction research and is not a clinically validated diagnostic product.

## 1. Introduction

Artificial Intelligence is a broad field concerned with systems that perform tasks associated with human intelligence. Machine Learning is a branch of AI in which algorithms learn patterns from data and use those patterns to make predictions.

This project applies supervised classification to structured clinical benchmark data. Users select a disease workflow, enter its required parameters and receive a model-generated result through a unified application.

## 2. Sustainable Development Goal alignment

### SDG 3 — Good Health and Well-being

The project relates to early risk identification and accessible preliminary screening research. It explores how structured clinical data and machine-learning models can support research into non-communicable disease risk.

Relevant targets discussed in the project presentation:
- SDG 3.4: reducing premature mortality from non-communicable diseases.
- SDG 3.8: access to quality healthcare services.

### SDG 9 — Industry, Innovation and Infrastructure

The project demonstrates an application of machine learning and web technologies to a healthcare research problem.

Relevant targets discussed in the presentation:
- SDG 9.1: reliable and resilient infrastructure.
- SDG 9.5: strengthening research and technological capabilities.

These are project-alignment statements, not claims of measured SDG impact.

## 3. Problem statement

Many machine-learning demonstrations focus on a single disease. Separate tools can make it difficult to compare workflows and provide a consistent user experience. The project addresses this problem by implementing disease-specific models within one application and recording their evaluation results using multiple classification metrics.

## 4. Research gap

The project presentation identifies four research gaps:

1. Single-disease focus: many systems are developed for individual conditions rather than a unified multi-disease platform.
2. Inconsistent evaluation: studies may use different preprocessing and evaluation procedures.
3. Limited unified systems: relatively few academic implementations combine multiple disease workflows, model comparison and web deployment.
4. Accessibility and decision support: there is a need for accessible preliminary screening tools that do not replace clinical diagnosis.

## 5. Project objectives

- Develop a unified platform for four disease-prediction workflows.
- Integrate Diabetes, Heart Disease, CKD and Breast Cancer models.
- Train and compare multiple machine-learning algorithms.
- Evaluate models using accuracy, precision, recall, F1-score and ROC-AUC.
- Integrate the selected models into a web application.
- Present results through an accessible user interface.

## 6. Literature survey

The following entries are transcribed from the supplied project presentation. Their bibliographic details should be checked against the original publications before academic submission.

| Study as listed in presentation | Year | Focus / method | Limitation noted in presentation |
|---|---:|---|---|
| Multiple Disease Prediction System — Parshant and A. Rathee | 2023 | Multiple diseases; KNN, SVM, Decision Tree, Random Forest, Logistic Regression | Limited model optimization and default parameters |
| Heart Disease Detection & Patients' Survival — A. Abdellatif et al. | 2022 | Heart disease; weighted Random Forest and feature selection | Single-disease focus |
| Diabetes Risk Prediction Using XGBoost — K. D. K. Wardhani and M. Akbar | 2022 | Diabetes; XGBoost and tree-based algorithms | Preprocessing protocol variation |
| Breast Cancer Detection on WDBC Dataset — A. F. M. Agarap | 2018 | Breast cancer; SVM, MLP, KNN, Decision Tree, XGBoost | Standalone model without deployed web application |
| CKD Prediction based on ML Algorithms — PMC / IEEE Research | 2023 | CKD; Random Forest, SVM, KNN and other algorithms | Sensitivity to missing-value imputation |

## 7. Proposed methodology

The project workflow is:

1. Collect public disease datasets.
2. Inspect and prepare the datasets.
3. Apply disease-specific preprocessing.
4. Train six machine-learning algorithms for each disease.
5. Evaluate models using multiple classification metrics.
6. Select a model for each disease workflow.
7. Integrate selected models into the application.
8. Accept user inputs and display prediction results.

## 8. Datasets

| Disease | Dataset identified in project materials | Rows | Features |
|---|---|---:|---:|
| Diabetes | Pima Indians Diabetes | 768 | 8 |
| Heart Disease | Cleveland Heart Disease | 303 | 13 |
| Chronic Kidney Disease | UCI Chronic Kidney Disease | 400 | 24 |
| Breast Cancer | Wisconsin Diagnostic | 569 | 30 |

These dataset counts are the recorded project metadata and should be checked against the exact dataset versions and preprocessing outputs used for each experiment.

## 9. Algorithms

Six algorithms are recorded for each disease:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Support Vector Machine
5. K-Nearest Neighbors
6. XGBoost

This gives 4 × 6 = **24 model experiment records** in the current comparison CSV.

## 10. Implementation and technology

The current repository structure and supplied build evidence identify the following application stack:

| Component | Technology |
|---|---|
| Frontend | React, Vite, JavaScript |
| Backend | Flask, Python |
| Machine learning | Scikit-learn, XGBoost |
| Data processing | Pandas, NumPy |
| Model persistence | Joblib |
| Automated testing | Pytest |
| Frontend build | Vite |

The supplied training logs report 41 passing pytest tests. The recorded frontend build completed successfully.

The presentation mentions Flask/Streamlit as proposed application technologies. This report uses the current repository's React/Vite and Flask stack rather than presenting Streamlit as the implemented frontend.

## 11. Selected model results

The following metrics are taken from `reports/results/best_models.json`.

| Disease | Selected model | Accuracy | Precision | Recall | F1-score | Test ROC-AUC | CV ROC-AUC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Diabetes | logistic_regression | 70.78% | 60.00% | 50.00% | 54.55% | 81.30% | 84.34% |
| Heart Disease | logistic_regression | 86.89% | 81.25% | 92.86% | 86.67% | 96.65% | 89.68% |
| Chronic Kidney Disease | logistic_regression | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% |
| Breast Cancer | logistic_regression | 96.49% | 97.50% | 92.86% | 95.12% | 99.60% | 99.58% |

## 12. Complete model comparison

All 24 rows below are generated from `reports/results/model_comparison.csv`.

| Disease | Algorithm | Dataset rows | Train rows | Test rows | CV ROC-AUC mean | CV ROC-AUC std | Accuracy | Precision | Recall | F1 | ROC-AUC | TN | FP | FN | TP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Breast Cancer | decision_tree | 569 | 455 | 114 | 0.9172 | 0.0375 | 92.98% | 90.48% | 90.48% | 90.48% | 92.46% | 68 | 4 | 4 | 38 |
| Breast Cancer | knn | 569 | 455 | 114 | 0.9871 | 0.0136 | 95.61% | 97.44% | 90.48% | 93.83% | 98.23% | 71 | 1 | 4 | 38 |
| Breast Cancer | logistic_regression | 569 | 455 | 114 | 0.9958 | 0.0047 | 96.49% | 97.50% | 92.86% | 95.12% | 99.60% | 71 | 1 | 3 | 39 |
| Breast Cancer | random_forest | 569 | 455 | 114 | 0.9880 | 0.0073 | 97.37% | 100.00% | 92.86% | 96.30% | 99.44% | 72 | 0 | 3 | 39 |
| Breast Cancer | svm | 569 | 455 | 114 | 0.9949 | 0.0050 | 97.37% | 100.00% | 92.86% | 96.30% | 99.47% | 72 | 0 | 3 | 39 |
| Breast Cancer | xgboost | 569 | 455 | 114 | 0.9928 | 0.0050 | 96.49% | 100.00% | 90.48% | 95.00% | 99.31% | 72 | 0 | 4 | 38 |
| Chronic Kidney Disease | decision_tree | 400 | 320 | 80 | 0.9692 | 0.0141 | 98.75% | 100.00% | 98.00% | 98.99% | 99.00% | 30 | 0 | 1 | 49 |
| Chronic Kidney Disease | knn | 400 | 320 | 80 | 0.9961 | 0.0049 | 97.50% | 100.00% | 96.00% | 97.96% | 99.93% | 30 | 0 | 2 | 48 |
| Chronic Kidney Disease | logistic_regression | 400 | 320 | 80 | 1.0000 | 0.0000 | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 30 | 0 | 0 | 50 |
| Chronic Kidney Disease | random_forest | 400 | 320 | 80 | 0.9998 | 0.0004 | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 30 | 0 | 0 | 50 |
| Chronic Kidney Disease | svm | 400 | 320 | 80 | 1.0000 | 0.0000 | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 30 | 0 | 0 | 50 |
| Chronic Kidney Disease | xgboost | 400 | 320 | 80 | 0.9983 | 0.0017 | 100.00% | 100.00% | 100.00% | 100.00% | 100.00% | 30 | 0 | 0 | 50 |
| Diabetes | decision_tree | 768 | 614 | 154 | 0.6510 | 0.0148 | 68.18% | 55.32% | 48.15% | 51.49% | 63.57% | 79 | 21 | 28 | 26 |
| Diabetes | knn | 768 | 614 | 154 | 0.7843 | 0.0373 | 75.32% | 66.00% | 61.11% | 63.46% | 78.99% | 83 | 17 | 21 | 33 |
| Diabetes | logistic_regression | 768 | 614 | 154 | 0.8434 | 0.0185 | 70.78% | 60.00% | 50.00% | 54.55% | 81.30% | 82 | 18 | 27 | 27 |
| Diabetes | random_forest | 768 | 614 | 154 | 0.8209 | 0.0209 | 74.03% | 65.91% | 53.70% | 59.18% | 81.60% | 85 | 15 | 25 | 29 |
| Diabetes | svm | 768 | 614 | 154 | 0.8333 | 0.0228 | 74.03% | 65.22% | 55.56% | 60.00% | 79.64% | 84 | 16 | 24 | 30 |
| Diabetes | xgboost | 768 | 614 | 154 | 0.7981 | 0.0192 | 74.68% | 65.31% | 59.26% | 62.14% | 83.09% | 83 | 17 | 22 | 32 |
| Heart Disease | decision_tree | 303 | 242 | 61 | 0.7490 | 0.0638 | 75.41% | 66.67% | 92.86% | 77.61% | 76.73% | 20 | 13 | 2 | 26 |
| Heart Disease | knn | 303 | 242 | 61 | 0.8832 | 0.0405 | 86.89% | 83.33% | 89.29% | 86.21% | 92.75% | 28 | 5 | 3 | 25 |
| Heart Disease | logistic_regression | 303 | 242 | 61 | 0.8968 | 0.0159 | 86.89% | 81.25% | 92.86% | 86.67% | 96.65% | 27 | 6 | 2 | 26 |
| Heart Disease | random_forest | 303 | 242 | 61 | 0.8934 | 0.0310 | 85.25% | 78.79% | 92.86% | 85.25% | 94.16% | 26 | 7 | 2 | 26 |
| Heart Disease | svm | 303 | 242 | 61 | 0.8798 | 0.0275 | 85.25% | 78.79% | 92.86% | 85.25% | 95.24% | 26 | 7 | 2 | 26 |
| Heart Disease | xgboost | 303 | 242 | 61 | 0.8737 | 0.0192 | 83.61% | 76.47% | 92.86% | 83.87% | 91.23% | 25 | 8 | 2 | 26 |

## 13. Cross-validation audit

The following summary is generated from `reports/results/repeated_cv_audit.csv`.

| Disease | Rows | Features | Accuracy mean | Precision mean | Recall mean | F1 mean | ROC-AUC mean | ROC-AUC std |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Diabetes | 768 | 8 | 76.69% | 71.35% | 55.80% | 62.42% | 83.54% | 0.0275 |
| Heart Disease | 303 | 13 | 83.53% | 84.59% | 79.00% | 81.42% | 90.30% | 0.0363 |
| Chronic Kidney Disease | 400 | 24 | 99.70% | 99.88% | 99.64% | 99.76% | 100.00% | 0.0001 |
| Breast Cancer | 569 | 30 | 97.89% | 98.56% | 95.76% | 97.11% | 99.48% | 0.0053 |

## 14. Evaluation metrics

- Accuracy: proportion of correct predictions.
- Precision: proportion of positive predictions that are correct.
- Recall: proportion of actual positive cases identified.
- F1-score: harmonic mean of precision and recall.
- ROC-AUC: ranking/discrimination measure across classification thresholds.
- Confusion matrix: true negatives, false positives, false negatives and true positives.

## 15. System design

The current implementation is organized into:
- React/Vite user interface.
- Flask API layer.
- Disease-specific input and prediction workflows.
- Saved model artifacts.
- Training and evaluation pipeline.
- Report and evaluation result files.

See [High-Level Design](02_hld.md), [Low-Level Design](03_lld.md), [Dataset Documentation](04_dataset_documentation.md) and [Preprocessing Methodology](05_preprocessing_methodology.md).

## 16. Conclusion

MediPredict AI demonstrates a unified academic web application for four disease-specific machine-learning workflows. The repository contains 24 experiment records, selected-model results, cross-validation summaries, saved model artifacts and an integrated frontend/backend application.

The results demonstrate benchmark-dataset performance only. They do not establish clinical reliability or suitability for patient diagnosis.

## 17. Limitations

- Benchmark datasets may not represent the wider population.
- Results depend on dataset quality, split strategy and preprocessing.
- The unusually high CKD metrics require independent leakage and duplicate-record investigation.
- The system is not clinically validated.
- Predictions must not be used as a substitute for professional medical advice or diagnosis.

## 18. Future scope

The project presentation identifies these possible extensions:

- Hyperparameter tuning and advanced feature selection.
- Testing on larger and more diverse datasets.
- Validation using independent real-world healthcare data.
- Explainable AI using SHAP or LIME.
- Deep-learning integration.
- IoT and wearable-device integration.
- Cloud deployment and electronic health record integration.

These are future directions, not claims of completed implementation.

## 19. References

The following references are reproduced from the project presentation:

1. H. O. Menge and P. Kuppuraj, "Machine Learning-Based Early Type 2 Diabetes Prediction," ICERCS, 2024. DOI: [10.1109/icercs63125.2024.10895576](https://doi.org/10.1109/icercs63125.2024.10895576).
2. N. Sharma and S. Sagar, "Diabetes Prediction Using Machine Learning Algorithms," ICAC2N, 2024. DOI: [10.1109/icac2n63387.2024.10894772](https://doi.org/10.1109/icac2n63387.2024.10894772).
3. S. Mall et al., "Prediction of Heart Disease using Machine Learning Technique," ICAC2N, 2024. DOI: [10.1109/icac2n63387.2024.10895125](https://doi.org/10.1109/icac2n63387.2024.10895125).
4. R. Sarang, V. Dabhi and A. Shah, "Breast Cancer Classification via the Use of ML and DL: A Comprehensive Review," ICACRS, 2024. DOI: [10.1109/icacrs62842.2024.10841677](https://doi.org/10.1109/icacrs62842.2024.10841677).
5. S. G. Jeevanantham et al., "Automated Breast Cancer Diagnosis Using Deep Learning CNN Models," ICERCS, 2024. DOI: [10.1109/icercs63125.2024.10895656](https://doi.org/10.1109/icercs63125.2024.10895656).

## 20. Supporting repository documentation

- [Literature Survey](01_literature_survey.md)
- [High-Level Design](02_hld.md)
- [Low-Level Design](03_lld.md)
- [Dataset Documentation](04_dataset_documentation.md)
- [Preprocessing Methodology](05_preprocessing_methodology.md)
- [Test Cases](06_test_cases.md)
- [SDG, Legal and Environmental Notes](09_sdg_legal_environmental.md)
- [Project Progress](11_monthly_project_progress.md)
- [Model Evaluation Evidence](MODEL_EVALUATION_EVIDENCE.md)
- [Screenshots Index](SCREENSHOTS.md)

---

**Academic use only. Not a clinically validated diagnostic system.**
