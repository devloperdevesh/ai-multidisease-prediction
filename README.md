# MediPredict AI
## AI-Based Medical Diagnosis System Using Machine Learning for Multi-Disease Prediction

Final Year Project | Department of Computer Science
ITS Engineering College, Greater Noida
Dr. A.P.J. Abdul Kalam Technical University, Lucknow

### Project Team
- Karan Kumar Tiwari
- Payal Chauhan
- Mamta Tiwari
- Devesh Chauhan

### 1. Project Overview
MediPredict AI is an academic multi-disease risk prediction research
prototype. It uses disease-specific machine learning models to assess
risk from structured clinical parameters.

The four conditions covered are:
1. Diabetes
2. Heart Disease
3. Chronic Kidney Disease (CKD)
4. Breast Cancer

The system is intended for preliminary research and decision support.
It does not provide a confirmed medical diagnosis.

### 2. Research Gap
Many existing systems focus on a single disease. There is a need for
a unified platform that combines multiple disease-specific models,
consistent model evaluation, model comparison and web deployment.

### 3. Project Objectives
- Develop a unified multi-disease prediction platform.
- Prepare public clinical benchmark datasets.
- Train and compare six machine learning algorithms per disease.
- Select the best model using evaluation results.
- Integrate prediction functionality into a web application.
- Present model evaluation and research results.

### 4. Dataset Inventory

| Disease | Dataset | Records | Features |
|---|---|---:|---:|
| Diabetes | Pima Indians Diabetes | 768 | 8 |
| Heart Disease | Cleveland Heart Disease | 303 | 13 |
| CKD | UCI Chronic Kidney Disease | 400 | 24 |
| Breast Cancer | Wisconsin Diagnostic | 569 | 30 |

These are public, de-identified benchmark datasets. They are not
live hospital records or a representative sample of all patients.

### 5. Machine Learning Algorithms

Six algorithms were trained for each of the four diseases:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Support Vector Machine (SVM)
5. K-Nearest Neighbors (KNN)
6. XGBoost

Total experiments: 4 x 6 = 24.

### 6. Best Model Results

| Disease | Selected Model | Accuracy | Precision | Recall | F1-score | Test ROC-AUC | CV ROC-AUC |
|---|---|---:|---:|---:|---:|---:|---:|
| Diabetes | Logistic Regression | 70.78% | 60.00% | 50.00% | 54.55% | 0.8130 | 0.8434 |
| Heart Disease | Logistic Regression | 86.89% | 81.25% | 92.86% | 86.67% | 0.9665 | 0.8968 |
| CKD | Logistic Regression | 100.00% | 100.00% | 100.00% | 100.00% | 1.0000 | 1.0000 |
| Breast Cancer | Logistic Regression | 96.49% | 97.50% | 92.86% | 95.12% | 0.9960 | 0.9958 |

Results are from the reported experiment run. They are not independent
clinical validation results. CKD's unusually high scores require
additional leakage and duplicate-record investigation.

Full 24-model comparison:
reports/results/model_comparison.csv

Other generated results:
- reports/results/model_training_results.json
- reports/results/best_models.json
- reports/results/dataset_audit.json
- reports/results/repeated_cv_audit.csv

### 7. Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Cross-validation ROC-AUC

### 8. Proposed System Architecture
1. Public dataset collection
2. Data preprocessing
3. Disease-specific model training
4. Model evaluation and comparison
5. Best model selection
6. Web application integration
7. Clinical parameter input
8. Risk prediction
9. Result display

### 9. Technology Stack
- Python
- Pandas and NumPy
- Scikit-learn
- XGBoost
- Flask
- React
- Vite
- HTML, CSS and JavaScript
- Joblib
- Pytest

### 10. Application Components
Frontend source includes:
- Disease selection and forms
- Prediction result components
- Research and analytics components
- Workspace and login components
- API service layer

Backend source includes:
- Dataset processing
- Model factory and training pipeline
- Prediction schemas and predictor
- Flask API and report storage

The presence of source components does not by itself establish
successful end-to-end frontend/API integration. See build and
runtime verification status before claiming deployment completion.

### 11. Testing
The reported backend test run completed with:
41 passed in 2.90 seconds.

Frontend production build status is recorded in the final
project verification report.

### 12. Research Limitations
- Public benchmark datasets are limited in size and population diversity.
- Model scores may vary with dataset split and preprocessing.
- CKD's perfect reported metrics require leakage investigation.
- Independent external validation is not established.
- The application is not clinically approved or validated.

### 13. Future Scope
- External clinical validation
- Explainable AI using SHAP/LIME
- Hyperparameter optimization
- Larger and more diverse datasets
- Cloud deployment
- Electronic Health Record integration
- IoT and wearable health data

### 14. Sustainable Development Goals
- SDG 3: Good Health and Well-being
- SDG 9: Industry, Innovation and Infrastructure

### 15. Reproduction Commands

Install Python dependencies:
python -m pip install -r requirements.txt

Train all models:
python -m src.training.train_all

Run backend tests:
python -m pytest -q

Install frontend dependencies:
cd frontend
npm.cmd install

Build frontend:
npm.cmd run build

### 16. Academic and Medical Disclaimer
MediPredict AI is an academic research prototype for preliminary
risk assessment. It must not be used as a substitute for a qualified
medical professional, laboratory testing or clinical diagnosis.



---
# Complete Model Evaluation Evidence

This section is generated directly from the experiment result files in `reports/results/`. Values are not manually estimated.

## 1. Complete 24-Experiment Model Comparison

Source: `reports/results/model_comparison.csv`  
Rows in source file: **24**

| disease | model | dataset_rows | feature_count | train_rows | test_rows | training_seconds | cv_roc_auc_mean | cv_roc_auc_std | accuracy | precision | recall | f1 | roc_auc | true_negative | false_positive | false_negative | true_positive | model_path |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| diabetes | logistic_regression | 768 | 8 | 614 | 154 | 0.0093 | 0.8433637873754153 | 0.0185495520715267 | 0.7077922077922078 | 0.6 | 0.5 | 0.5454545454545454 | 0.812962962962963 | 82 | 18 | 27 | 27 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\diabetes\logistic_regression.joblib |
| diabetes | decision_tree | 768 | 8 | 614 | 154 | 0.008 | 0.6510063676633444 | 0.0147804316938096 | 0.6818181818181818 | 0.5531914893617021 | 0.4814814814814814 | 0.5148514851485149 | 0.6357407407407407 | 79 | 21 | 28 | 26 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\diabetes\decision_tree.joblib |
| diabetes | random_forest | 768 | 8 | 614 | 154 | 0.6831 | 0.8209482281284608 | 0.0208999509766387 | 0.7402597402597403 | 0.6590909090909091 | 0.5370370370370371 | 0.5918367346938775 | 0.8160185185185185 | 85 | 15 | 25 | 29 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\diabetes\random_forest.joblib |
| diabetes | svm | 768 | 8 | 614 | 154 | 0.0539 | 0.8333084163898116 | 0.0228034589568724 | 0.7402597402597403 | 0.6521739130434783 | 0.5555555555555556 | 0.6 | 0.7963888888888889 | 84 | 16 | 24 | 30 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\diabetes\svm.joblib |
| diabetes | knn | 768 | 8 | 614 | 154 | 0.0059 | 0.7843320874861572 | 0.0372814326353469 | 0.7532467532467533 | 0.66 | 0.6111111111111112 | 0.6346153846153846 | 0.7899074074074074 | 83 | 17 | 21 | 33 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\diabetes\knn.joblib |
| diabetes | xgboost | 768 | 8 | 614 | 154 | 0.2035 | 0.7981063122923587 | 0.0191533641759488 | 0.7467532467532467 | 0.6530612244897959 | 0.5925925925925926 | 0.6213592233009708 | 0.8309259259259258 | 83 | 17 | 22 | 32 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\diabetes\xgboost.joblib |
| heart | logistic_regression | 303 | 13 | 242 | 61 | 0.0186 | 0.8967844554801075 | 0.0159206607910756 | 0.8688524590163934 | 0.8125 | 0.9285714285714286 | 0.8666666666666667 | 0.9664502164502164 | 27 | 6 | 2 | 26 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\heart\logistic_regression.joblib |
| heart | decision_tree | 303 | 13 | 242 | 61 | 0.0116 | 0.7490456403499882 | 0.0637845035007264 | 0.7540983606557377 | 0.6666666666666666 | 0.9285714285714286 | 0.7761194029850746 | 0.7673160173160173 | 20 | 13 | 2 | 26 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\heart\decision_tree.joblib |
| heart | random_forest | 303 | 13 | 242 | 61 | 0.5242 | 0.893442789094963 | 0.0309944456343565 | 0.8524590163934426 | 0.7878787878787878 | 0.9285714285714286 | 0.8524590163934426 | 0.9415584415584416 | 26 | 7 | 2 | 26 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\heart\random_forest.joblib |
| heart | svm | 303 | 13 | 242 | 61 | 0.0203 | 0.8798064254585996 | 0.0274883035571603 | 0.8524590163934426 | 0.7878787878787878 | 0.9285714285714286 | 0.8524590163934426 | 0.9523809523809524 | 26 | 7 | 2 | 26 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\heart\svm.joblib |
| heart | knn | 303 | 13 | 242 | 61 | 0.0151 | 0.8831545668502191 | 0.040499907500973 | 0.8688524590163934 | 0.8333333333333334 | 0.8928571428571429 | 0.8620689655172413 | 0.9274891774891776 | 28 | 5 | 3 | 25 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\heart\knn.joblib |
| heart | xgboost | 303 | 13 | 242 | 61 | 0.2055 | 0.8736889519498214 | 0.0192295599297639 | 0.8360655737704918 | 0.7647058823529411 | 0.9285714285714286 | 0.8387096774193549 | 0.9123376623376624 | 25 | 8 | 2 | 26 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\heart\xgboost.joblib |
| ckd | logistic_regression | 400 | 24 | 320 | 80 | 0.0244 | 1.0 | 0.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 30 | 0 | 0 | 50 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\ckd\logistic_regression.joblib |
| ckd | decision_tree | 400 | 24 | 320 | 80 | 0.0229 | 0.9691666666666666 | 0.0140929454377397 | 0.9875 | 1.0 | 0.98 | 0.98989898989899 | 0.99 | 30 | 0 | 1 | 49 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\ckd\decision_tree.joblib |
| ckd | random_forest | 400 | 24 | 320 | 80 | 0.66 | 0.9997916666666666 | 0.0004166666666666 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 30 | 0 | 0 | 50 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\ckd\random_forest.joblib |
| ckd | svm | 400 | 24 | 320 | 80 | 0.0238 | 1.0 | 0.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 30 | 0 | 0 | 50 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\ckd\svm.joblib |
| ckd | knn | 400 | 24 | 320 | 80 | 0.0121 | 0.9961458333333332 | 0.0049256626739736 | 0.975 | 1.0 | 0.96 | 0.979591836734694 | 0.9993333333333334 | 30 | 0 | 2 | 48 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\ckd\knn.joblib |
| ckd | xgboost | 400 | 24 | 320 | 80 | 0.195 | 0.9983333333333334 | 0.0016925080009658 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 30 | 0 | 0 | 50 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\ckd\xgboost.joblib |
| breast_cancer | logistic_regression | 569 | 30 | 455 | 114 | 0.0135 | 0.9957688338493292 | 0.0046656984749049 | 0.9649122807017544 | 0.975 | 0.9285714285714286 | 0.951219512195122 | 0.996031746031746 | 71 | 1 | 3 | 39 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\breast_cancer\logistic_regression.joblib |
| breast_cancer | decision_tree | 569 | 30 | 455 | 114 | 0.0121 | 0.9172342621259032 | 0.0375421661005599 | 0.9298245614035088 | 0.9047619047619048 | 0.9047619047619048 | 0.9047619047619048 | 0.9246031746031744 | 68 | 4 | 4 | 38 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\breast_cancer\decision_tree.joblib |
| breast_cancer | random_forest | 569 | 30 | 455 | 114 | 0.4226 | 0.9879772961816304 | 0.0072819431836194 | 0.9736842105263158 | 1.0 | 0.9285714285714286 | 0.9629629629629628 | 0.9943783068783068 | 72 | 0 | 3 | 39 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\breast_cancer\random_forest.joblib |
| breast_cancer | svm | 569 | 30 | 455 | 114 | 0.032 | 0.9949432404540764 | 0.0049642986463594 | 0.9736842105263158 | 1.0 | 0.9285714285714286 | 0.9629629629629628 | 0.9947089947089948 | 72 | 0 | 3 | 39 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\breast_cancer\svm.joblib |
| breast_cancer | knn | 569 | 30 | 455 | 114 | 0.0139 | 0.9871001031991744 | 0.0135815759557168 | 0.956140350877193 | 0.9743589743589745 | 0.9047619047619048 | 0.9382716049382716 | 0.982308201058201 | 71 | 1 | 4 | 38 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\breast_cancer\knn.joblib |
| breast_cancer | xgboost | 569 | 30 | 455 | 114 | 0.2199 | 0.9927760577915375 | 0.0050133984732677 | 0.9649122807017544 | 1.0 | 0.9047619047619048 | 0.95 | 0.9930555555555556 | 72 | 0 | 4 | 38 | C:\Users\OS\OneDrive\Music\Desktop\ai-multidisease-prediction\models\breast_cancer\xgboost.joblib |
> Verification: 24 experiment records are present in the source comparison CSV.

### Algorithm count per disease
| disease | Unique algorithms |
| --- | --- |
| breast_cancer | 6 |
| ckd | 6 |
| diabetes | 6 |
| heart | 6 |
## 2. Cross-Validation Results

Source: `reports/results/repeated_cv_audit.csv`  
Rows in source file: **4**

| disease | rows | features | accuracy_mean | accuracy_std | precision_mean | precision_std | recall_mean | recall_std | f1_mean | f1_std | roc_auc_mean | roc_auc_std |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| diabetes | 768 | 8 | 0.7668983957219251 | 0.0289498502502554 | 0.7134537328460558 | 0.0576444540214651 | 0.5580293501048218 | 0.0666320041974218 | 0.6241683171265832 | 0.0543731660526463 | 0.8354218728162125 | 0.0274739767908912 |
| heart | 303 | 13 | 0.8352950819672131 | 0.0443442434404304 | 0.84590869840038 | 0.0646508031894698 | 0.7899735449735449 | 0.07232694405873 | 0.8141779023488196 | 0.0505980852595125 | 0.9030348124098124 | 0.0363372209129084 |
| ckd | 400 | 24 | 0.997 | 0.0064031242374328 | 0.9988156862745098 | 0.0046878674788674 | 0.9964000000000002 | 0.008662563131083 | 0.9975836759186124 | 0.0051629519943425 | 0.9999733333333332 | 0.0001306394529484 |
| breast_cancer | 569 | 30 | 0.9789147647880764 | 0.0141682597059254 | 0.9856168866112144 | 0.0151416701108991 | 0.9575526024363232 | 0.0335753896052761 | 0.9710523331362088 | 0.0197972836575841 | 0.99484400589584 | 0.0053363373657416 |
## 3. Selected Best Models — Source JSON

Source: `reports/results/best_models.json`

The following JSON is copied from the actual best-model result file. It is retained as source evidence; no metric values are recalculated or invented here.

```json
{
  "diabetes": {
    "model": "logistic_regression",
    "cv_roc_auc_mean": 0.8433637873754153,
    "test_accuracy": 0.7077922077922078,
    "test_precision": 0.6,
    "test_recall": 0.5,
    "test_f1": 0.5454545454545454,
    "test_roc_auc": 0.812962962962963,
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\diabetes\\logistic_regression.joblib"
  },
  "heart": {
    "model": "logistic_regression",
    "cv_roc_auc_mean": 0.8967844554801075,
    "test_accuracy": 0.8688524590163934,
    "test_precision": 0.8125,
    "test_recall": 0.9285714285714286,
    "test_f1": 0.8666666666666667,
    "test_roc_auc": 0.9664502164502164,
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\heart\\logistic_regression.joblib"
  },
  "ckd": {
    "model": "logistic_regression",
    "cv_roc_auc_mean": 1.0,
    "test_accuracy": 1.0,
    "test_precision": 1.0,
    "test_recall": 1.0,
    "test_f1": 1.0,
    "test_roc_auc": 1.0,
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\ckd\\logistic_regression.joblib"
  },
  "breast_cancer": {
    "model": "logistic_regression",
    "cv_roc_auc_mean": 0.9957688338493291,
    "test_accuracy": 0.9649122807017544,
    "test_precision": 0.975,
    "test_recall": 0.9285714285714286,
    "test_f1": 0.9512195121951219,
    "test_roc_auc": 0.996031746031746,
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\breast_cancer\\logistic_regression.joblib"
  }
}
```

## 4. Model Artifact Verification

Found **24** `.joblib` model artifacts.
| Disease | Model artifact | Size (bytes) |
| --- | --- | --- |
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
## 5. Reproducibility and Evidence Files

| Evidence | File |
|---|---|
| All model experiment metrics | `reports/results/model_comparison.csv` |
| Cross-validation audit | `reports/results/repeated_cv_audit.csv` |
| Selected best models | `reports/results/best_models.json` |
| Training details | `reports/results/model_training_results.json` |
| Dataset audit | `reports/results/dataset_audit.json` |
| Real prediction test records | `reports/results/four_real_prediction_tests.csv` |

To reproduce:

```powershell
python -m src.training.train_all
python -m pytest -q
```

**Research limitation:** These are benchmark-dataset experiment results.
They do not establish clinical validity or guarantee predictions for
individual patients. CKD's unusually high metrics require independent
leakage and duplicate-record checks.


---

# Additional Source Evidence

## model_training_results.json

```json
[
  {
    "disease": "diabetes",
    "model": "logistic_regression",
    "dataset_rows": 768,
    "feature_count": 8,
    "train_rows": 614,
    "test_rows": 154,
    "training_seconds": 0.0093,
    "cv_roc_auc_mean": 0.8433637873754153,
    "cv_roc_auc_std": 0.018549552071526722,
    "test_metrics": {
      "accuracy": 0.7077922077922078,
      "precision": 0.6,
      "recall": 0.5,
      "f1": 0.5454545454545454,
      "roc_auc": 0.812962962962963,
      "true_negative": 82,
      "false_positive": 18,
      "false_negative": 27,
      "true_positive": 27
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\diabetes\\logistic_regression.joblib",
    "target": "Outcome"
  },
  {
    "disease": "diabetes",
    "model": "decision_tree",
    "dataset_rows": 768,
    "feature_count": 8,
    "train_rows": 614,
    "test_rows": 154,
    "training_seconds": 0.008,
    "cv_roc_auc_mean": 0.6510063676633444,
    "cv_roc_auc_std": 0.014780431693809631,
    "test_metrics": {
      "accuracy": 0.6818181818181818,
      "precision": 0.5531914893617021,
      "recall": 0.48148148148148145,
      "f1": 0.5148514851485149,
      "roc_auc": 0.6357407407407407,
      "true_negative": 79,
      "false_positive": 21,
      "false_negative": 28,
      "true_positive": 26
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\diabetes\\decision_tree.joblib",
    "target": "Outcome"
  },
  {
    "disease": "diabetes",
    "model": "random_forest",
    "dataset_rows": 768,
    "feature_count": 8,
    "train_rows": 614,
    "test_rows": 154,
    "training_seconds": 0.6831,
    "cv_roc_auc_mean": 0.8209482281284608,
    "cv_roc_auc_std": 0.020899950976638763,
    "test_metrics": {
      "accuracy": 0.7402597402597403,
      "precision": 0.6590909090909091,
      "recall": 0.5370370370370371,
      "f1": 0.5918367346938775,
      "roc_auc": 0.8160185185185185,
      "true_negative": 85,
      "false_positive": 15,
      "false_negative": 25,
      "true_positive": 29
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\diabetes\\random_forest.joblib",
    "target": "Outcome"
  },
  {
    "disease": "diabetes",
    "model": "svm",
    "dataset_rows": 768,
    "feature_count": 8,
    "train_rows": 614,
    "test_rows": 154,
    "training_seconds": 0.0539,
    "cv_roc_auc_mean": 0.8333084163898116,
    "cv_roc_auc_std": 0.022803458956872403,
    "test_metrics": {
      "accuracy": 0.7402597402597403,
      "precision": 0.6521739130434783,
      "recall": 0.5555555555555556,
      "f1": 0.6,
      "roc_auc": 0.7963888888888889,
      "true_negative": 84,
      "false_positive": 16,
      "false_negative": 24,
      "true_positive": 30
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\diabetes\\svm.joblib",
    "target": "Outcome"
  },
  {
    "disease": "diabetes",
    "model": "knn",
    "dataset_rows": 768,
    "feature_count": 8,
    "train_rows": 614,
    "test_rows": 154,
    "training_seconds": 0.0059,
    "cv_roc_auc_mean": 0.7843320874861572,
    "cv_roc_auc_std": 0.03728143263534694,
    "test_metrics": {
      "accuracy": 0.7532467532467533,
      "precision": 0.66,
      "recall": 0.6111111111111112,
      "f1": 0.6346153846153846,
      "roc_auc": 0.7899074074074074,
      "true_negative": 83,
      "false_positive": 17,
      "false_negative": 21,
      "true_positive": 33
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\diabetes\\knn.joblib",
    "target": "Outcome"
  },
  {
    "disease": "diabetes",
    "model": "xgboost",
    "dataset_rows": 768,
    "feature_count": 8,
    "train_rows": 614,
    "test_rows": 154,
    "training_seconds": 0.2035,
    "cv_roc_auc_mean": 0.7981063122923587,
    "cv_roc_auc_std": 0.01915336417594889,
    "test_metrics": {
      "accuracy": 0.7467532467532467,
      "precision": 0.6530612244897959,
      "recall": 0.5925925925925926,
      "f1": 0.6213592233009708,
      "roc_auc": 0.8309259259259258,
      "true_negative": 83,
      "false_positive": 17,
      "false_negative": 22,
      "true_positive": 32
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\diabetes\\xgboost.joblib",
    "target": "Outcome"
  },
  {
    "disease": "heart",
    "model": "logistic_regression",
    "dataset_rows": 303,
    "feature_count": 13,
    "train_rows": 242,
    "test_rows": 61,
    "training_seconds": 0.0186,
    "cv_roc_auc_mean": 0.8967844554801075,
    "cv_roc_auc_std": 0.015920660791075677,
    "test_metrics": {
      "accuracy": 0.8688524590163934,
      "precision": 0.8125,
      "recall": 0.9285714285714286,
      "f1": 0.8666666666666667,
      "roc_auc": 0.9664502164502164,
      "true_negative": 27,
      "false_positive": 6,
      "false_negative": 2,
      "true_positive": 26
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\heart\\logistic_regression.joblib",
    "target": "num"
  },
  {
    "disease": "heart",
    "model": "decision_tree",
    "dataset_rows": 303,
    "feature_count": 13,
    "train_rows": 242,
    "test_rows": 61,
    "training_seconds": 0.0116,
    "cv_roc_auc_mean": 0.7490456403499882,
    "cv_roc_auc_std": 0.06378450350072647,
    "test_metrics": {
      "accuracy": 0.7540983606557377,
      "precision": 0.6666666666666666,
      "recall": 0.9285714285714286,
      "f1": 0.7761194029850746,
      "roc_auc": 0.7673160173160173,
      "true_negative": 20,
      "false_positive": 13,
      "false_negative": 2,
      "true_positive": 26
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\heart\\decision_tree.joblib",
    "target": "num"
  },
  {
    "disease": "heart",
    "model": "random_forest",
    "dataset_rows": 303,
    "feature_count": 13,
    "train_rows": 242,
    "test_rows": 61,
    "training_seconds": 0.5242,
    "cv_roc_auc_mean": 0.893442789094963,
    "cv_roc_auc_std": 0.030994445634356597,
    "test_metrics": {
      "accuracy": 0.8524590163934426,
      "precision": 0.7878787878787878,
      "recall": 0.9285714285714286,
      "f1": 0.8524590163934426,
      "roc_auc": 0.9415584415584416,
      "true_negative": 26,
      "false_positive": 7,
      "false_negative": 2,
      "true_positive": 26
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\heart\\random_forest.joblib",
    "target": "num"
  },
  {
    "disease": "heart",
    "model": "svm",
    "dataset_rows": 303,
    "feature_count": 13,
    "train_rows": 242,
    "test_rows": 61,
    "training_seconds": 0.0203,
    "cv_roc_auc_mean": 0.8798064254585996,
    "cv_roc_auc_std": 0.027488303557160348,
    "test_metrics": {
      "accuracy": 0.8524590163934426,
      "precision": 0.7878787878787878,
      "recall": 0.9285714285714286,
      "f1": 0.8524590163934426,
      "roc_auc": 0.9523809523809523,
      "true_negative": 26,
      "false_positive": 7,
      "false_negative": 2,
      "true_positive": 26
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\heart\\svm.joblib",
    "target": "num"
  },
  {
    "disease": "heart",
    "model": "knn",
    "dataset_rows": 303,
    "feature_count": 13,
    "train_rows": 242,
    "test_rows": 61,
    "training_seconds": 0.0151,
    "cv_roc_auc_mean": 0.8831545668502191,
    "cv_roc_auc_std": 0.04049990750097307,
    "test_metrics": {
      "accuracy": 0.8688524590163934,
      "precision": 0.8333333333333334,
      "recall": 0.8928571428571429,
      "f1": 0.8620689655172413,
      "roc_auc": 0.9274891774891775,
      "true_negative": 28,
      "false_positive": 5,
      "false_negative": 3,
      "true_positive": 25
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\heart\\knn.joblib",
    "target": "num"
  },
  {
    "disease": "heart",
    "model": "xgboost",
    "dataset_rows": 303,
    "feature_count": 13,
    "train_rows": 242,
    "test_rows": 61,
    "training_seconds": 0.2055,
    "cv_roc_auc_mean": 0.8736889519498214,
    "cv_roc_auc_std": 0.019229559929763967,
    "test_metrics": {
      "accuracy": 0.8360655737704918,
      "precision": 0.7647058823529411,
      "recall": 0.9285714285714286,
      "f1": 0.8387096774193549,
      "roc_auc": 0.9123376623376623,
      "true_negative": 25,
      "false_positive": 8,
      "false_negative": 2,
      "true_positive": 26
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\heart\\xgboost.joblib",
    "target": "num"
  },
  {
    "disease": "ckd",
    "model": "logistic_regression",
    "dataset_rows": 400,
    "feature_count": 24,
    "train_rows": 320,
    "test_rows": 80,
    "training_seconds": 0.0244,
    "cv_roc_auc_mean": 1.0,
    "cv_roc_auc_std": 0.0,
    "test_metrics": {
      "accuracy": 1.0,
      "precision": 1.0,
      "recall": 1.0,
      "f1": 1.0,
      "roc_auc": 1.0,
      "true_negative": 30,
      "false_positive": 0,
      "false_negative": 0,
      "true_positive": 50
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\ckd\\logistic_regression.joblib",
    "target": "class"
  },
  {
    "disease": "ckd",
    "model": "decision_tree",
    "dataset_rows": 400,
    "feature_count": 24,
    "train_rows": 320,
    "test_rows": 80,
    "training_seconds": 0.0229,
    "cv_roc_auc_mean": 0.9691666666666666,
    "cv_roc_auc_std": 0.014092945437739798,
    "test_metrics": {
      "accuracy": 0.9875,
      "precision": 1.0,
      "recall": 0.98,
      "f1": 0.98989898989899,
      "roc_auc": 0.99,
      "true_negative": 30,
      "false_positive": 0,
      "false_negative": 1,
      "true_positive": 49
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\ckd\\decision_tree.joblib",
    "target": "class"
  },
  {
    "disease": "ckd",
    "model": "random_forest",
    "dataset_rows": 400,
    "feature_count": 24,
    "train_rows": 320,
    "test_rows": 80,
    "training_seconds": 0.66,
    "cv_roc_auc_mean": 0.9997916666666666,
    "cv_roc_auc_std": 0.00041666666666668746,
    "test_metrics": {
      "accuracy": 1.0,
      "precision": 1.0,
      "recall": 1.0,
      "f1": 1.0,
      "roc_auc": 1.0,
      "true_negative": 30,
      "false_positive": 0,
      "false_negative": 0,
      "true_positive": 50
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\ckd\\random_forest.joblib",
    "target": "class"
  },
  {
    "disease": "ckd",
    "model": "svm",
    "dataset_rows": 400,
    "feature_count": 24,
    "train_rows": 320,
    "test_rows": 80,
    "training_seconds": 0.0238,
    "cv_roc_auc_mean": 1.0,
    "cv_roc_auc_std": 0.0,
    "test_metrics": {
      "accuracy": 1.0,
      "precision": 1.0,
      "recall": 1.0,
      "f1": 1.0,
      "roc_auc": 1.0,
      "true_negative": 30,
      "false_positive": 0,
      "false_negative": 0,
      "true_positive": 50
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\ckd\\svm.joblib",
    "target": "class"
  },
  {
    "disease": "ckd",
    "model": "knn",
    "dataset_rows": 400,
    "feature_count": 24,
    "train_rows": 320,
    "test_rows": 80,
    "training_seconds": 0.0121,
    "cv_roc_auc_mean": 0.9961458333333333,
    "cv_roc_auc_std": 0.00492566267397369,
    "test_metrics": {
      "accuracy": 0.975,
      "precision": 1.0,
      "recall": 0.96,
      "f1": 0.9795918367346939,
      "roc_auc": 0.9993333333333334,
      "true_negative": 30,
      "false_positive": 0,
      "false_negative": 2,
      "true_positive": 48
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\ckd\\knn.joblib",
    "target": "class"
  },
  {
    "disease": "ckd",
    "model": "xgboost",
    "dataset_rows": 400,
    "feature_count": 24,
    "train_rows": 320,
    "test_rows": 80,
    "training_seconds": 0.195,
    "cv_roc_auc_mean": 0.9983333333333334,
    "cv_roc_auc_std": 0.0016925080009658382,
    "test_metrics": {
      "accuracy": 1.0,
      "precision": 1.0,
      "recall": 1.0,
      "f1": 1.0,
      "roc_auc": 1.0,
      "true_negative": 30,
      "false_positive": 0,
      "false_negative": 0,
      "true_positive": 50
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\ckd\\xgboost.joblib",
    "target": "class"
  },
  {
    "disease": "breast_cancer",
    "model": "logistic_regression",
    "dataset_rows": 569,
    "feature_count": 30,
    "train_rows": 455,
    "test_rows": 114,
    "training_seconds": 0.0135,
    "cv_roc_auc_mean": 0.9957688338493291,
    "cv_roc_auc_std": 0.004665698474904977,
    "test_metrics": {
      "accuracy": 0.9649122807017544,
      "precision": 0.975,
      "recall": 0.9285714285714286,
      "f1": 0.9512195121951219,
      "roc_auc": 0.996031746031746,
      "true_negative": 71,
      "false_positive": 1,
      "false_negative": 3,
      "true_positive": 39
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\breast_cancer\\logistic_regression.joblib",
    "target": "Diagnosis"
  },
  {
    "disease": "breast_cancer",
    "model": "decision_tree",
    "dataset_rows": 569,
    "feature_count": 30,
    "train_rows": 455,
    "test_rows": 114,
    "training_seconds": 0.0121,
    "cv_roc_auc_mean": 0.9172342621259031,
    "cv_roc_auc_std": 0.0375421661005599,
    "test_metrics": {
      "accuracy": 0.9298245614035088,
      "precision": 0.9047619047619048,
      "recall": 0.9047619047619048,
      "f1": 0.9047619047619048,
      "roc_auc": 0.9246031746031745,
      "true_negative": 68,
      "false_positive": 4,
      "false_negative": 4,
      "true_positive": 38
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\breast_cancer\\decision_tree.joblib",
    "target": "Diagnosis"
  },
  {
    "disease": "breast_cancer",
    "model": "random_forest",
    "dataset_rows": 569,
    "feature_count": 30,
    "train_rows": 455,
    "test_rows": 114,
    "training_seconds": 0.4226,
    "cv_roc_auc_mean": 0.9879772961816305,
    "cv_roc_auc_std": 0.007281943183619418,
    "test_metrics": {
      "accuracy": 0.9736842105263158,
      "precision": 1.0,
      "recall": 0.9285714285714286,
      "f1": 0.9629629629629629,
      "roc_auc": 0.9943783068783069,
      "true_negative": 72,
      "false_positive": 0,
      "false_negative": 3,
      "true_positive": 39
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\breast_cancer\\random_forest.joblib",
    "target": "Diagnosis"
  },
  {
    "disease": "breast_cancer",
    "model": "svm",
    "dataset_rows": 569,
    "feature_count": 30,
    "train_rows": 455,
    "test_rows": 114,
    "training_seconds": 0.032,
    "cv_roc_auc_mean": 0.9949432404540763,
    "cv_roc_auc_std": 0.00496429864635942,
    "test_metrics": {
      "accuracy": 0.9736842105263158,
      "precision": 1.0,
      "recall": 0.9285714285714286,
      "f1": 0.9629629629629629,
      "roc_auc": 0.9947089947089947,
      "true_negative": 72,
      "false_positive": 0,
      "false_negative": 3,
      "true_positive": 39
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\breast_cancer\\svm.joblib",
    "target": "Diagnosis"
  },
  {
    "disease": "breast_cancer",
    "model": "knn",
    "dataset_rows": 569,
    "feature_count": 30,
    "train_rows": 455,
    "test_rows": 114,
    "training_seconds": 0.0139,
    "cv_roc_auc_mean": 0.9871001031991744,
    "cv_roc_auc_std": 0.013581575955716877,
    "test_metrics": {
      "accuracy": 0.956140350877193,
      "precision": 0.9743589743589743,
      "recall": 0.9047619047619048,
      "f1": 0.9382716049382716,
      "roc_auc": 0.982308201058201,
      "true_negative": 71,
      "false_positive": 1,
      "false_negative": 4,
      "true_positive": 38
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\breast_cancer\\knn.joblib",
    "target": "Diagnosis"
  },
  {
    "disease": "breast_cancer",
    "model": "xgboost",
    "dataset_rows": 569,
    "feature_count": 30,
    "train_rows": 455,
    "test_rows": 114,
    "training_seconds": 0.2199,
    "cv_roc_auc_mean": 0.9927760577915377,
    "cv_roc_auc_std": 0.0050133984732677024,
    "test_metrics": {
      "accuracy": 0.9649122807017544,
      "precision": 1.0,
      "recall": 0.9047619047619048,
      "f1": 0.95,
      "roc_auc": 0.9930555555555555,
      "true_negative": 72,
      "false_positive": 0,
      "false_negative": 4,
      "true_positive": 38
    },
    "model_path": "C:\\Users\\OS\\OneDrive\\Music\\Desktop\\ai-multidisease-prediction\\models\\breast_cancer\\xgboost.joblib",
    "target": "Diagnosis"
  }
]
```

## dataset_audit.json

```json
{
  "diabetes": {
    "disease": "diabetes",
    "file": "data\\raw\\diabetes\\pima_diabetes.csv",
    "rows": 768,
    "columns": 9,
    "column_names": [
      "Pregnancies",
      "Glucose",
      "BloodPressure",
      "SkinThickness",
      "Insulin",
      "BMI",
      "DiabetesPedigreeFunction",
      "Age",
      "Outcome"
    ],
    "target": "Outcome",
    "target_found": true,
    "dtypes": {
      "Pregnancies": "int64",
      "Glucose": "int64",
      "BloodPressure": "int64",
      "SkinThickness": "int64",
      "Insulin": "int64",
      "BMI": "float64",
      "DiabetesPedigreeFunction": "float64",
      "Age": "int64",
      "Outcome": "int64"
    },
    "missing_values": {},
    "suspicious_values": {},
    "duplicate_rows": 0,
    "numeric_columns": [
      "Pregnancies",
      "Glucose",
      "BloodPressure",
      "SkinThickness",
      "Insulin",
      "BMI",
      "DiabetesPedigreeFunction",
      "Age",
      "Outcome"
    ],
    "categorical_columns": [],
    "target_distribution": {
      "0": 500,
      "1": 268
    }
  },
  "heart": {
    "disease": "heart",
    "file": "data\\raw\\heart\\uci_heart_disease.csv",
    "rows": 303,
    "columns": 14,
    "column_names": [
      "age",
      "sex",
      "cp",
      "trestbps",
      "chol",
      "fbs",
      "restecg",
      "thalach",
      "exang",
      "oldpeak",
      "slope",
      "ca",
      "thal",
      "num"
    ],
    "target": "num",
    "target_found": true,
    "dtypes": {
      "age": "int64",
      "sex": "int64",
      "cp": "int64",
      "trestbps": "int64",
      "chol": "int64",
      "fbs": "int64",
      "restecg": "int64",
      "thalach": "int64",
      "exang": "int64",
      "oldpeak": "float64",
      "slope": "int64",
      "ca": "float64",
      "thal": "float64",
      "num": "int64"
    },
    "missing_values": {
      "ca": 4,
      "thal": 2
    },
    "suspicious_values": {},
    "duplicate_rows": 0,
    "numeric_columns": [
      "age",
      "sex",
      "cp",
      "trestbps",
      "chol",
      "fbs",
      "restecg",
      "thalach",
      "exang",
      "oldpeak",
      "slope",
      "ca",
      "thal",
      "num"
    ],
    "categorical_columns": [],
    "target_distribution": {
      "0": 164,
      "1": 55,
      "2": 36,
      "3": 35,
      "4": 13
    }
  },
  "ckd": {
    "disease": "ckd",
    "file": "data\\raw\\ckd\\uci_chronic_kidney_disease.csv",
    "rows": 400,
    "columns": 25,
    "column_names": [
      "age",
      "bp",
      "sg",
      "al",
      "su",
      "rbc",
      "pc",
      "pcc",
      "ba",
      "bgr",
      "bu",
      "sc",
      "sod",
      "pot",
      "hemo",
      "pcv",
      "wbcc",
      "rbcc",
      "htn",
      "dm",
      "cad",
      "appet",
      "pe",
      "ane",
      "class"
    ],
    "target": "class",
    "target_found": true,
    "dtypes": {
      "age": "float64",
      "bp": "float64",
      "sg": "float64",
      "al": "float64",
      "su": "float64",
      "rbc": "object",
      "pc": "object",
      "pcc": "object",
      "ba": "object",
      "bgr": "float64",
      "bu": "float64",
      "sc": "float64",
      "sod": "float64",
      "pot": "float64",
      "hemo": "float64",
      "pcv": "float64",
      "wbcc": "float64",
      "rbcc": "float64",
      "htn": "object",
      "dm": "object",
      "cad": "object",
      "appet": "object",
      "pe": "object",
      "ane": "object",
      "class": "object"
    },
    "missing_values": {
      "age": 9,
      "bp": 12,
      "sg": 47,
      "al": 46,
      "su": 49,
      "rbc": 152,
      "pc": 65,
      "pcc": 4,
      "ba": 4,
      "bgr": 44,
      "bu": 19,
      "sc": 17,
      "sod": 87,
      "pot": 88,
      "hemo": 52,
      "pcv": 71,
      "wbcc": 106,
      "rbcc": 131,
      "htn": 2,
      "dm": 2,
      "cad": 2,
      "appet": 1,
      "pe": 1,
      "ane": 1
    },
    "suspicious_values": {},
    "duplicate_rows": 0,
    "numeric_columns": [
      "age",
      "bp",
      "sg",
      "al",
      "su",
      "bgr",
      "bu",
      "sc",
      "sod",
      "pot",
      "hemo",
      "pcv",
      "wbcc",
      "rbcc"
    ],
    "categorical_columns": [
      "rbc",
      "pc",
      "pcc",
      "ba",
      "htn",
      "dm",
      "cad",
      "appet",
      "pe",
      "ane",
      "class"
    ],
    "target_distribution": {
      "ckd": 250,
      "notckd": 150
    }
  },
  "breast_cancer": {
    "disease": "breast_cancer",
    "file": "data\\raw\\breast_cancer\\uci_breast_cancer_diagnostic.csv",
    "rows": 569,
    "columns": 31,
    "column_names": [
      "radius1",
      "texture1",
      "perimeter1",
      "area1",
      "smoothness1",
      "compactness1",
      "concavity1",
      "concave_points1",
      "symmetry1",
      "fractal_dimension1",
      "radius2",
      "texture2",
      "perimeter2",
      "area2",
      "smoothness2",
      "compactness2",
      "concavity2",
      "concave_points2",
      "symmetry2",
      "fractal_dimension2",
      "radius3",
      "texture3",
      "perimeter3",
      "area3",
      "smoothness3",
      "compactness3",
      "concavity3",
      "concave_points3",
      "symmetry3",
      "fractal_dimension3",
      "Diagnosis"
    ],
    "target": "Diagnosis",
    "target_found": true,
    "dtypes": {
      "radius1": "float64",
      "texture1": "float64",
      "perimeter1": "float64",
      "area1": "float64",
      "smoothness1": "float64",
      "compactness1": "float64",
      "concavity1": "float64",
      "concave_points1": "float64",
      "symmetry1": "float64",
      "fractal_dimension1": "float64",
      "radius2": "float64",
      "texture2": "float64",
      "perimeter2": "float64",
      "area2": "float64",
      "smoothness2": "float64",
      "compactness2": "float64",
      "concavity2": "float64",
      "concave_points2": "float64",
      "symmetry2": "float64",
      "fractal_dimension2": "float64",
      "radius3": "float64",
      "texture3": "float64",
      "perimeter3": "float64",
      "area3": "float64",
      "smoothness3": "float64",
      "compactness3": "float64",
      "concavity3": "float64",
      "concave_points3": "float64",
      "symmetry3": "float64",
      "fractal_dimension3": "float64",
      "Diagnosis": "object"
    },
    "missing_values": {},
    "suspicious_values": {},
    "duplicate_rows": 0,
    "numeric_columns": [
      "radius1",
      "texture1",
      "perimeter1",
      "area1",
      "smoothness1",
      "compactness1",
      "concavity1",
      "concave_points1",
      "symmetry1",
      "fractal_dimension1",
      "radius2",
      "texture2",
      "perimeter2",
      "area2",
      "smoothness2",
      "compactness2",
      "concavity2",
      "concave_points2",
      "symmetry2",
      "fractal_dimension2",
      "radius3",
      "texture3",
      "perimeter3",
      "area3",
      "smoothness3",
      "compactness3",
      "concavity3",
      "concave_points3",
      "symmetry3",
      "fractal_dimension3"
    ],
    "categorical_columns": [
      "Diagnosis"
    ],
    "target_distribution": {
      "B": 357,
      "M": 212
    }
  }
}
```

## four_real_prediction_tests.csv

Source rows: **4**

| disease       | dataset                                   |   source_row_index |   actual_label | actual_label_meaning   |   predicted_label | prediction_correct   | model               |   positive_class_probability |   positive_class_probability_percent | test_status   |
|:--------------|:------------------------------------------|-------------------:|---------------:|:-----------------------|------------------:|:---------------------|:--------------------|-----------------------------:|-------------------------------------:|:--------------|
| diabetes      | Pima Indians Diabetes Dataset             |                 44 |              0 | Negative class         |                 1 | False                | logistic_regression |                     0.6097   |                                60.97 | PASS          |
| heart         | UCI Cleveland Heart Disease Dataset       |                219 |              0 | Negative class         |                 0 | True                 | logistic_regression |                     0.217746 |                                21.77 | PASS          |
| ckd           | UCI Chronic Kidney Disease Dataset        |                342 |              0 | Negative class         |                 0 | True                 | logistic_regression |                     0.003303 |                                 0.33 | PASS          |
| breast_cancer | Wisconsin Diagnostic Breast Cancer (WDBC) |                120 |              0 | Negative class         |                 0 | True                 | logistic_regression |                     0.000365 |                                 0.04 | PASS          |

## four_real_prediction_tests.json

```json
[
  {
    "disease": "diabetes",
    "dataset": "Pima Indians Diabetes Dataset",
    "source_row_index": 44,
    "actual_label": 0,
    "actual_label_meaning": "Negative class",
    "predicted_label": 1,
    "prediction_correct": false,
    "model": "logistic_regression",
    "positive_class_probability": 0.6097,
    "positive_class_probability_percent": 60.97,
    "test_status": "PASS"
  },
  {
    "disease": "heart",
    "dataset": "UCI Cleveland Heart Disease Dataset",
    "source_row_index": 219,
    "actual_label": 0,
    "actual_label_meaning": "Negative class",
    "predicted_label": 0,
    "prediction_correct": true,
    "model": "logistic_regression",
    "positive_class_probability": 0.217746,
    "positive_class_probability_percent": 21.77,
    "test_status": "PASS"
  },
  {
    "disease": "ckd",
    "dataset": "UCI Chronic Kidney Disease Dataset",
    "source_row_index": 342,
    "actual_label": 0,
    "actual_label_meaning": "Negative class",
    "predicted_label": 0,
    "prediction_correct": true,
    "model": "logistic_regression",
    "positive_class_probability": 0.003303,
    "positive_class_probability_percent": 0.33,
    "test_status": "PASS"
  },
  {
    "disease": "breast_cancer",
    "dataset": "Wisconsin Diagnostic Breast Cancer (WDBC)",
    "source_row_index": 120,
    "actual_label": 0,
    "actual_label_meaning": "Negative class",
    "predicted_label": 0,
    "prediction_correct": true,
    "model": "logistic_regression",
    "positive_class_probability": 0.000365,
    "positive_class_probability_percent": 0.04,
    "test_status": "PASS"
  }
]
```

## repeated_cv_audit.json

```json
[
  {
    "disease": "diabetes",
    "rows": 768,
    "features": 8,
    "accuracy_mean": 0.7668983957219251,
    "accuracy_std": 0.028949850250255454,
    "precision_mean": 0.7134537328460558,
    "precision_std": 0.05764445402146511,
    "recall_mean": 0.5580293501048218,
    "recall_std": 0.06663200419742187,
    "f1_mean": 0.6241683171265832,
    "f1_std": 0.05437316605264636,
    "roc_auc_mean": 0.8354218728162125,
    "roc_auc_std": 0.027473976790891242
  },
  {
    "disease": "heart",
    "rows": 303,
    "features": 13,
    "accuracy_mean": 0.8352950819672131,
    "accuracy_std": 0.044344243440430454,
    "precision_mean": 0.84590869840038,
    "precision_std": 0.06465080318946985,
    "recall_mean": 0.7899735449735449,
    "recall_std": 0.07232694405873005,
    "f1_mean": 0.8141779023488196,
    "f1_std": 0.05059808525951252,
    "roc_auc_mean": 0.9030348124098124,
    "roc_auc_std": 0.036337220912908405
  },
  {
    "disease": "ckd",
    "rows": 400,
    "features": 24,
    "accuracy_mean": 0.997,
    "accuracy_std": 0.00640312423743284,
    "precision_mean": 0.9988156862745098,
    "precision_std": 0.004687867478867483,
    "recall_mean": 0.9964000000000002,
    "recall_std": 0.008662563131083094,
    "f1_mean": 0.9975836759186123,
    "f1_std": 0.0051629519943425925,
    "roc_auc_mean": 0.9999733333333333,
    "roc_auc_std": 0.00013063945294844353
  },
  {
    "disease": "breast_cancer",
    "rows": 569,
    "features": 30,
    "accuracy_mean": 0.9789147647880764,
    "accuracy_std": 0.014168259705925447,
    "precision_mean": 0.9856168866112145,
    "precision_std": 0.015141670110899142,
    "recall_mean": 0.9575526024363233,
    "recall_std": 0.0335753896052761,
    "f1_mean": 0.9710523331362089,
    "f1_std": 0.01979728365758416,
    "roc_auc_mean": 0.99484400589584,
    "roc_auc_std": 0.0053363373657416635
  }
]
```

