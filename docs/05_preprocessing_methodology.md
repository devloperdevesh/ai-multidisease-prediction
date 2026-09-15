# Preprocessing Methodology

## 1. Objective

The preprocessing stage converts heterogeneous healthcare datasets into model-ready inputs while reducing data leakage.

## 2. General Workflow

Raw Dataset
|
v
Validation
|
v
Cleaning
|
v
Target Transformation
|
v
Feature / Target Split
|
v
Train / Test Split
|
v
Fit Preprocessor on Training Data
|
v
Transform Data
|
v
Model Training

## 3. Diabetes

Zero values will be treated as missing for:

- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI

Zero will not automatically be treated as missing for:

- Pregnancies
- Age
- DiabetesPedigreeFunction

Missing numerical values will be handled using training-data statistics.

## 4. Heart Disease

The original target contains five levels.

Binary transformation:

0 -> 0
1, 2, 3, 4 -> 1

Missing values in ca and thal will be handled by the preprocessing pipeline.

## 5. CKD

CKD contains numerical and categorical variables.

Numerical features:

- Imputation
- Standard scaling

Categorical features:

- Most-frequent imputation
- One-hot encoding
- Unknown-category handling

## 6. Breast Cancer

The Diagnosis target will be converted to binary classification.

B -> 0
M -> 1

The numerical features will be standardized where required by the selected model pipeline.

## 7. Leakage Prevention

Preprocessing transformations must be fitted only on training data.

The test set must not influence:

- Imputation statistics
- Scaling parameters
- Encoding
- Feature selection

## 8. Class Distribution

Class distributions will be inspected for each disease.

Accuracy will not be the only evaluation metric.

## 9. Reproducibility

A common random state is maintained in project configuration.

Model parameters, preprocessing decisions and experimental results will be recorded.

## 10. Validation

Preprocessing will be validated before large-scale model training.
