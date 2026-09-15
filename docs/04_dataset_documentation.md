# Dataset Documentation

## 1. Dataset Summary

| Disease | Dataset | Rows | Columns | Target |
|---|---|---:|---:|---|
| Diabetes | Pima Diabetes | 768 | 9 | Outcome |
| Heart Disease | UCI Heart Disease | 303 | 14 | num |
| CKD | UCI Chronic Kidney Disease | 400 | 25 | class |
| Breast Cancer | UCI Breast Cancer Diagnostic | 569 | 31 | Diagnosis |

## 2. Diabetes

The diabetes dataset contains 768 records and 9 columns.

Features:

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

Target:

Outcome

The dataset contains 500 records with target 0 and 268 records with target 1.

The audit found no pandas NaN values, no blank values, no question-mark values and no duplicate rows.

Several physiological measurements contain zero values and require domain-aware preprocessing.

## 3. Heart Disease

The heart dataset contains 303 records and 14 columns.

The target num contains:

0 = 164
1 = 55
2 = 36
3 = 35
4 = 13

For binary prediction:

0 -> 0
1, 2, 3, 4 -> 1

Missing values identified:

ca = 4
thal = 2

## 4. Chronic Kidney Disease

The CKD dataset contains 400 records and 25 columns.

Target:

ckd = 250
notckd = 150

The dataset contains numerical and categorical variables with substantial missing values.

Numerical features include:

- age
- bp
- sg
- al
- su
- bgr
- bu
- sc
- sod
- pot
- hemo
- pcv
- wbcc
- rbcc

Categorical features include:

- rbc
- pc
- pcc
- ba
- htn
- dm
- cad
- appet
- pe
- ane

## 5. Breast Cancer

The breast cancer diagnostic dataset contains 569 records and 31 columns.

It contains 30 numerical diagnostic features and the Diagnosis target.

Target:

B = 357
M = 212

The target will be encoded for binary classification.

The audit found no pandas NaN values, no blank values, no question-mark values and no duplicate rows.

## 6. Dataset Audit

The project audit checks:

- Shape
- Column names
- Data types
- Missing values
- Blank values
- Question-mark values
- Duplicate rows
- Numeric columns
- Categorical columns
- Target distribution
- Numeric statistics

Generated reports:

reports/results/dataset_audit.json
reports/results/dataset_audit.md

## 7. Data Governance

Raw datasets are stored locally and excluded from normal Git commits.

Dataset acquisition:

scripts/download_datasets.py

Dataset auditing:

scripts/audit_datasets.py

Dataset source and licensing information will be retained in the final academic report according to applicable source terms.
