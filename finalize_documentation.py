from pathlib import Path
import pandas as pd
import json

root = Path(".")
results = root / "reports" / "results"
docs = root / "docs"
docs.mkdir(exist_ok=True)

comparison = pd.read_csv(results / "model_comparison.csv")
cv = pd.read_csv(results / "repeated_cv_audit.csv")

best = json.loads(
    (results / "best_models.json").read_text(encoding="utf-8-sig")
)

if len(comparison) != 24:
    raise SystemExit(f"Expected 24 experiments; found {len(comparison)}")

if comparison.groupby("disease")["model"].nunique().min() != 6:
    raise SystemExit("Six algorithms per disease could not be verified.")

names = {
    "diabetes": "Diabetes",
    "heart": "Heart Disease",
    "ckd": "Chronic Kidney Disease",
    "breast_cancer": "Breast Cancer"
}

def pct(x):
    return f"{float(x)*100:.2f}%"

def table(headers, rows):
    out = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |"
    ]
    for row in rows:
        out.append("| " + " | ".join(str(x).replace("|", r"\|") for x in row) + " |")
    return "\n".join(out)

selected_rows = []
for disease, record in best.items():
    selected_rows.append([
        names.get(disease, disease),
        record.get("model", "N/A"),
        pct(record.get("test_accuracy", 0)),
        pct(record.get("test_precision", 0)),
        pct(record.get("test_recall", 0)),
        pct(record.get("test_f1", 0)),
        pct(record.get("test_roc_auc", 0)),
        pct(record.get("cv_roc_auc_mean", 0))
    ])

all_rows = []
for _, r in comparison.sort_values(["disease", "model"]).iterrows():
    all_rows.append([
        names.get(r["disease"], r["disease"]),
        r["model"],
        r["dataset_rows"],
        r["train_rows"],
        r["test_rows"],
        f'{float(r["cv_roc_auc_mean"]):.4f}',
        f'{float(r["cv_roc_auc_std"]):.4f}',
        pct(r["accuracy"]),
        pct(r["precision"]),
        pct(r["recall"]),
        pct(r["f1"]),
        pct(r["roc_auc"]),
        r["true_negative"],
        r["false_positive"],
        r["false_negative"],
        r["true_positive"]
    ])

cv_rows = []
for _, r in cv.iterrows():
    cv_rows.append([
        names.get(r["disease"], r["disease"]),
        r["rows"],
        r["features"],
        pct(r["accuracy_mean"]),
        pct(r["precision_mean"]),
        pct(r["recall_mean"]),
        pct(r["f1_mean"]),
        pct(r["roc_auc_mean"]),
        f'{float(r["roc_auc_std"]):.4f}'
    ])

report = f'''# MediPredict AI — Final Year Project Report

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

{table(
    ["Disease", "Selected model", "Accuracy", "Precision", "Recall", "F1-score", "Test ROC-AUC", "CV ROC-AUC"],
    selected_rows
)}

## 12. Complete model comparison

All 24 rows below are generated from `reports/results/model_comparison.csv`.

{table(
    ["Disease", "Algorithm", "Dataset rows", "Train rows", "Test rows",
     "CV ROC-AUC mean", "CV ROC-AUC std", "Accuracy", "Precision",
     "Recall", "F1", "ROC-AUC", "TN", "FP", "FN", "TP"],
    all_rows
)}

## 13. Cross-validation audit

The following summary is generated from `reports/results/repeated_cv_audit.csv`.

{table(
    ["Disease", "Rows", "Features", "Accuracy mean", "Precision mean",
     "Recall mean", "F1 mean", "ROC-AUC mean", "ROC-AUC std"],
    cv_rows
)}

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
'''

(docs / "PROJECT_REPORT.md").write_text(report, encoding="utf-8")

# Generate a conservative implementation status report.
# File existence is not treated as proof that a feature is fully implemented.
status = '''# Implementation Status and Evidence Boundaries

This document separates repository evidence from proposed or unverified capabilities.

## Evidence confirmed from supplied project outputs

| Item | Evidence |
|---|---|
| Four disease categories | Dataset and model comparison records |
| Six algorithms per disease | 24 rows in model comparison CSV |
| 24 experiment records | `reports/results/model_comparison.csv` |
| Selected model results | `reports/results/best_models.json` |
| Cross-validation summary | `reports/results/repeated_cv_audit.csv` |
| Saved model artifacts | Earlier repository audit reported 24 Joblib artifacts |
| Backend tests | Supplied terminal output: 41 passed |
| Frontend build | Earlier supplied terminal output: Vite build succeeded |
| UI evidence | Screenshots in `docs/screenshots/` |

## Current repository architecture

- Frontend source: `frontend/src/`
- API source: `app/api/server.py`
- Prediction source: `src/prediction/`
- Training source: `src/training/`
- Data preparation: `src/data/`
- Automated tests: `tests/`

## Claims requiring further source-level validation

The existence of a file or a keyword match alone does not prove a feature is fully implemented.

| Capability | Documentation treatment |
|---|---|
| Feature selection | Do not claim a specific method without tracing the active training pipeline |
| Class-imbalance handling / SMOTE | Do not claim until the training code and experiment configuration are verified |
| Prediction probability and risk bands | Verify API response and frontend display together |
| User feedback loop | Treat as future scope unless a working persistence/training flow is demonstrated |
| SHAP / LIME | Future scope unless integrated and tested |
| Streamlit frontend | Not the current documented frontend; current stack is React/Vite + Flask |
| Clinical validation | Not established |

## Medical and research limitations

The results are benchmark-dataset experiments. They are not clinical validation. The unusually high CKD metrics require independent checks for leakage, duplicates, preprocessing contamination and split integrity before making strong performance claims.
'''
(docs / "IMPLEMENTATION_STATUS.md").write_text(status, encoding="utf-8")

# Update README without replacing its existing content.
readme_path = root / "README.md"
readme = readme_path.read_text(encoding="utf-8-sig")

# Fix exact CKD screenshot reference, only if the wrong name is present.
readme = readme.replace(
    "02C_MediPredict_AI_CKD_Form.png",
    "02C_MediPredict_AI_CKD_Form..png"
)

index = '''## Academic and technical documentation

| Document | Contents |
|---|---|
| [Final Year Project Report](docs/PROJECT_REPORT.md) | Introduction, SDG alignment, literature survey, research gap, objectives, methodology, implementation, results, conclusion and references |
| [Implementation Status](docs/IMPLEMENTATION_STATUS.md) | Verified evidence, architecture and claims requiring further validation |
| [High-Level Design](docs/02_hld.md) | System architecture |
| [Low-Level Design](docs/03_lld.md) | Component-level design |
| [Dataset Documentation](docs/04_dataset_documentation.md) | Dataset information |
| [Preprocessing Methodology](docs/05_preprocessing_methodology.md) | Data preparation |
| [Literature Survey](docs/01_literature_survey.md) | Related work |
| [Test Cases](docs/06_test_cases.md) | Test documentation |
| [Model Evaluation Evidence](docs/MODEL_EVALUATION_EVIDENCE.md) | All 24 model experiments and evaluation records |
| [Screenshots Index](docs/SCREENSHOTS.md) | Application screenshots |

'''

marker = "## Academic and technical documentation"
if marker in readme:
    readme = readme.split(marker)[0].rstrip() + "\n\n"

readme = readme.rstrip() + "\n\n" + index
readme_path.write_text(readme, encoding="utf-8")

print("Academic report generated:", docs / "PROJECT_REPORT.md")
print("Implementation status generated:", docs / "IMPLEMENTATION_STATUS.md")
print("README documentation index updated.")
print("Experiment rows:", len(comparison))
print("Cross-validation rows:", len(cv))
print("Selected-model records:", len(best))
print("CKD screenshot path checked.")
