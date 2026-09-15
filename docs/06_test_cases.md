# Test Cases

## 1. Purpose

Testing verifies data processing, model utilities, prediction behaviour, API validation and user-facing workflows.

## 2. Current Automated Tests

The current foundational test suite contains 12 tests.

Latest verified baseline:

12/12 tests passed.

## 3. Functional Test Cases

| ID | Test Case | Expected Result |
|---|---|---|
| TC-01 | Load diabetes dataset | Dataset loads |
| TC-02 | Load heart dataset | Dataset loads |
| TC-03 | Load CKD dataset | Dataset loads |
| TC-04 | Load breast cancer dataset | Dataset loads |
| TC-05 | Missing target column | Validation error |
| TC-06 | Empty dataset | Validation error |
| TC-07 | Missing numerical values | Imputation handles values |
| TC-08 | Missing categorical values | Imputation handles values |
| TC-09 | Unknown category | Safely handled |
| TC-10 | Valid prediction | Prediction returned |
| TC-11 | Empty prediction | Validation error |
| TC-12 | Binary probability model | Probability returned when supported |
| TC-13 | Invalid disease | API error |
| TC-14 | Missing API field | Validation error |
| TC-15 | Valid diabetes request | Result returned |
| TC-16 | Valid heart request | Result returned |
| TC-17 | Valid CKD request | Result returned |
| TC-18 | Valid breast cancer request | Result returned |

## 4. ML Evaluation

Each trained model will be evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC

## 5. UI Tests

The final UI should validate:

- Required fields
- Numeric validation
- Loading state
- Result rendering
- Error handling
- Responsive layout
- Disclaimer visibility
- Voice availability

## 6. Acceptance Criteria

A prediction workflow is ready when:

1. Valid input is accepted.
2. Invalid input is rejected safely.
3. Correct model is loaded.
4. Prediction is generated.
5. Result is displayed clearly.
6. Probability is shown when supported.
7. Medical disclaimer is visible.
