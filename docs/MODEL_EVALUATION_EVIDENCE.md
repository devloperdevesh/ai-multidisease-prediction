# MediPredict AI — Model Evaluation Evidence

> **Medical disclaimer:** This document records academic machine-learning experiments. The results are not clinical validation and must not be used for medical diagnosis or treatment.

## 1. Project Summary

MediPredict AI contains four disease-specific classification workflows and six evaluated algorithms per disease.

| Disease | Dataset | Records | Features |
|---|---|---:|---:|
| Diabetes | Pima Indians Diabetes | 768 | 8 |
| Heart Disease | Cleveland Heart Disease | 303 | 13 |
| CKD | UCI Chronic Kidney Disease | 400 | 24 |
| Breast Cancer | Wisconsin Diagnostic | 569 | 30 |

## 2. Experiment Inventory

Source: eports/results/model_comparison.csv

- Experiment records: **24**
- Disease categories: **4**
- Algorithms per disease: **6**

| Disease | Algorithm | Dataset | Features | Train | Test | CV ROC-AUC | Accuracy | Precision | Recall | F1 | Test ROC-AUC | TN | FP | FN | TP |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| diabetes | logistic_regression | 768 | 8 | 614 | 154 | 0.8434 | 70.78% | 60.00% | 50.00% | 54.55% | 0.8130 | 82 | 18 | 27 | 27 |
| diabetes | decision_tree | 768 | 8 | 614 | 154 | 0.6510 | 68.18% | 55.32% | 48.15% | 51.49% | 0.6357 | 79 | 21 | 28 | 26 |
| diabetes | random_forest | 768 | 8 | 614 | 154 | 0.8209 | 74.03% | 65.91% | 53.70% | 59.18% | 0.8160 | 85 | 15 | 25 | 29 |
| diabetes | svm | 768 | 8 | 614 | 154 | 0.8333 | 74.03% | 65.22% | 55.56% | 60.00% | 0.7964 | 84 | 16 | 24 | 30 |
| diabetes | knn | 768 | 8 | 614 | 154 | 0.7843 | 75.32% | 66.00% | 61.11% | 63.46% | 0.7899 | 83 | 17 | 21 | 33 |
| diabetes | xgboost | 768 | 8 | 614 | 154 | 0.7981 | 74.68% | 65.31% | 59.26% | 62.14% | 0.8309 | 83 | 17 | 22 | 32 |
| heart | logistic_regression | 303 | 13 | 242 | 61 | 0.8968 | 86.89% | 81.25% | 92.86% | 86.67% | 0.9665 | 27 | 6 | 2 | 26 |
| heart | decision_tree | 303 | 13 | 242 | 61 | 0.7490 | 75.41% | 66.67% | 92.86% | 77.61% | 0.7673 | 20 | 13 | 2 | 26 |
| heart | random_forest | 303 | 13 | 242 | 61 | 0.8934 | 85.25% | 78.79% | 92.86% | 85.25% | 0.9416 | 26 | 7 | 2 | 26 |
| heart | svm | 303 | 13 | 242 | 61 | 0.8798 | 85.25% | 78.79% | 92.86% | 85.25% | 0.9524 | 26 | 7 | 2 | 26 |
| heart | knn | 303 | 13 | 242 | 61 | 0.8832 | 86.89% | 83.33% | 89.29% | 86.21% | 0.9275 | 28 | 5 | 3 | 25 |
| heart | xgboost | 303 | 13 | 242 | 61 | 0.8737 | 83.61% | 76.47% | 92.86% | 83.87% | 0.9123 | 25 | 8 | 2 | 26 |
| ckd | logistic_regression | 400 | 24 | 320 | 80 | 1.0000 | 100.00% | 100.00% | 100.00% | 100.00% | 1.0000 | 30 | 0 | 0 | 50 |
| ckd | decision_tree | 400 | 24 | 320 | 80 | 0.9692 | 98.75% | 100.00% | 98.00% | 98.99% | 0.9900 | 30 | 0 | 1 | 49 |
| ckd | random_forest | 400 | 24 | 320 | 80 | 0.9998 | 100.00% | 100.00% | 100.00% | 100.00% | 1.0000 | 30 | 0 | 0 | 50 |
| ckd | svm | 400 | 24 | 320 | 80 | 1.0000 | 100.00% | 100.00% | 100.00% | 100.00% | 1.0000 | 30 | 0 | 0 | 50 |
| ckd | knn | 400 | 24 | 320 | 80 | 0.9961 | 97.50% | 100.00% | 96.00% | 97.96% | 0.9993 | 30 | 0 | 2 | 48 |
| ckd | xgboost | 400 | 24 | 320 | 80 | 0.9983 | 100.00% | 100.00% | 100.00% | 100.00% | 1.0000 | 30 | 0 | 0 | 50 |
| breast_cancer | logistic_regression | 569 | 30 | 455 | 114 | 0.9958 | 96.49% | 97.50% | 92.86% | 95.12% | 0.9960 | 71 | 1 | 3 | 39 |
| breast_cancer | decision_tree | 569 | 30 | 455 | 114 | 0.9172 | 92.98% | 90.48% | 90.48% | 90.48% | 0.9246 | 68 | 4 | 4 | 38 |
| breast_cancer | random_forest | 569 | 30 | 455 | 114 | 0.9880 | 97.37% | 100.00% | 92.86% | 96.30% | 0.9944 | 72 | 0 | 3 | 39 |
| breast_cancer | svm | 569 | 30 | 455 | 114 | 0.9949 | 97.37% | 100.00% | 92.86% | 96.30% | 0.9947 | 72 | 0 | 3 | 39 |
| breast_cancer | knn | 569 | 30 | 455 | 114 | 0.9871 | 95.61% | 97.44% | 90.48% | 93.83% | 0.9823 | 71 | 1 | 4 | 38 |
| breast_cancer | xgboost | 569 | 30 | 455 | 114 | 0.9928 | 96.49% | 100.00% | 90.48% | 95.00% | 0.9931 | 72 | 0 | 4 | 38 |

## 3. Selected Model Summary

Source: eports/results/best_models.json

| Disease | Model | Accuracy | Precision | Recall | F1 | Test ROC-AUC | CV ROC-AUC |
|---|---|---:|---:|---:|---:|---:|---:|
| Diabetes | logistic_regression | 70.78% | 60.00% | 50.00% | 54.55% | 0.8130 | 0.8434 |
| Heart Disease | logistic_regression | 86.89% | 81.25% | 92.86% | 86.67% | 0.9665 | 0.8968 |
| Chronic Kidney Disease | logistic_regression | 100.00% | 100.00% | 100.00% | 100.00% | 1.0000 | 1.0000 |
| Breast Cancer | logistic_regression | 96.49% | 97.50% | 92.86% | 95.12% | 0.9960 | 0.9958 |

## 4. Repeated Cross-Validation Audit

Source: eports/results/repeated_cv_audit.csv

| Disease | Rows | Features | Accuracy | Precision | Recall | F1 | ROC-AUC | ROC-AUC Std |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| diabetes | 768 | 8 | 76.69% | 71.35% | 55.80% | 62.42% | 0.8354 | 0.0275 |
| heart | 303 | 13 | 83.53% | 84.59% | 79.00% | 81.42% | 0.9030 | 0.0363 |
| ckd | 400 | 24 | 99.70% | 99.88% | 99.64% | 99.76% | 1.0000 | 0.0001 |
| breast_cancer | 569 | 30 | 97.89% | 98.56% | 95.76% | 97.11% | 0.9948 | 0.0053 |

## 5. Model Artifact Inventory

The following inventory is generated from the .joblib files currently present under models/.

Artifacts found: **24**

| Disease | Model artifact | Size (bytes) |
|---|---|---:|
| breast_cancer | decision_tree.joblib | 9012 |
| breast_cancer | knn.joblib | 117647 |
| breast_cancer | logistic_regression.joblib | 5082 |
| breast_cancer | random_forest.joblib | 998699 |
| breast_cancer | svm.joblib | 33510 |
| breast_cancer | xgboost.joblib | 308932 |
| ckd | decision_tree.joblib | 10324 |
| ckd | knn.joblib | 553583 |
| ckd | logistic_regression.joblib | 10058 |
| ckd | random_forest.joblib | 1134763 |
| ckd | svm.joblib | 125878 |
| ckd | xgboost.joblib | 273903 |
| diabetes | decision_tree.joblib | 21284 |
| diabetes | knn.joblib | 97137 |
| diabetes | logistic_regression.joblib | 3258 |
| diabetes | random_forest.joblib | 5084395 |
| diabetes | svm.joblib | 33430 |
| diabetes | xgboost.joblib | 477235 |
| heart | decision_tree.joblib | 12260 |
| heart | knn.joblib | 45310 |
| heart | logistic_regression.joblib | 4858 |
| heart | random_forest.joblib | 2288459 |
| heart | svm.joblib | 31654 |
| heart | xgboost.joblib | 436342 |

## 6. Reproducibility Files

| Evidence | Source |
|---|---|
| Model comparison | eports/results/model_comparison.csv |
| Repeated CV audit | eports/results/repeated_cv_audit.csv |
| Best models | eports/results/best_models.json |
| Training details | eports/results/model_training_results.json |
| Dataset audit | eports/results/dataset_audit.json |
| Prediction test records | eports/results/four_real_prediction_tests.csv |

## 7. Reproduction

`powershell
python -m src.training.train_all
python -m pytest -q
`

Re-training may change model artifacts and metrics. Record the dataset version, random seed, split strategy, preprocessing pipeline and software versions for reproducibility.

## 8. Interpretation and Limitations

- Accuracy, precision, recall, F1-score and ROC-AUC describe performance on the recorded evaluation data.
- Cross-validation values summarize the reported validation procedure; they are not a substitute for independent external validation.
- The CKD results are unusually high and require careful investigation for duplicate records, target leakage, preprocessing leakage and dataset split integrity.
- Model artifact presence does not prove clinical readiness or production reliability.
- No independent clinical validation is established by these experiment records.

**Conclusion:** These results document a multi-model academic benchmark experiment. Further reproducibility checks and independent validation are necessary before any real-world medical use.
