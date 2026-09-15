# Low-Level Design (LLD)

## 1. Project Module Structure

src/
    config.py
    data/
        loader.py
        preprocessing.py
    models/
        model_factory.py
    prediction/
        predictor.py
    training/
        train.py
        evaluate.py
        model_selection.py

app/
    app.py
    templates/
        index.html
    static/
        css/
            style.css
        js/
            app.js

tests/
    test_models.py
    test_prediction.py
    test_preprocessing.py

## 2. Configuration Module

src/config.py contains:

- Project root
- Dataset directories
- Model directories
- Results directory
- Disease names
- Model names
- Random state

## 3. Data Loader

src/data/loader.py provides:

- Dataset discovery
- CSV loading
- Excel loading
- Column normalization
- Disease-specific dataset loading
- File validation

## 4. Preprocessing Module

src/data/preprocessing.py provides:

- Feature-target separation
- Numerical feature detection
- Categorical feature detection
- Numerical imputation
- Categorical imputation
- Standard scaling
- One-hot encoding

## 5. Model Factory

The model factory provides:

- Logistic Regression
- Decision Tree
- Random Forest
- SVM
- KNN
- XGBoost

## 6. Training Module

The training module will:

1. Load dataset
2. Validate target
3. Separate features and target
4. Split training and testing data
5. Fit preprocessing on training data
6. Train candidate models
7. Evaluate models
8. Select best model
9. Save model artifact

## 7. Evaluation Module

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

## 8. Prediction Module

src/prediction/predictor.py loads trained model artifacts using joblib.

Prediction flow:

Input
|
v
Loaded Model
|
v
Class Prediction
|
v
Probability when supported
|
v
Prediction Response

## 9. Planned API

GET /api/health

Purpose:
Check backend health.

GET /api/diseases

Purpose:
Return supported diseases.

POST /api/predict/<disease>

Purpose:
Generate preliminary risk prediction.

## 10. Error Handling

The system should handle:

- Missing input fields
- Invalid numerical values
- Unsupported disease names
- Missing model artifacts
- Prediction failures

## 11. Testing

The existing test suite covers foundational preprocessing, model and prediction functionality.

Additional API and UI tests will be added during integration.
