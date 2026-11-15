from pathlib import Path
import pandas as pd
import json

ROOT = Path(".")
RESULTS = ROOT / "reports" / "results"

comparison = pd.read_csv(RESULTS / "model_comparison.csv")
cv = pd.read_csv(RESULTS / "repeated_cv_audit.csv")

with open(RESULTS / "best_models.json", encoding="utf-8-sig") as f:
    best_json = json.load(f)

if len(comparison) != 24:
    raise SystemExit(f"Expected 24 model records, got {len(comparison)}")

if comparison["disease"].nunique() != 4:
    raise SystemExit("Expected four disease categories.")

if comparison.groupby("disease")["model"].nunique().min() != 6:
    raise SystemExit("Expected six algorithms per disease.")

def fmt_percent(value):
    try:
        return f"{float(value) * 100:.2f}%"
    except (ValueError, TypeError):
        return "N/A"

def fmt_number(value):
    try:
        return f"{float(value):.4f}"
    except (ValueError, TypeError):
        return "N/A"

def md_table(headers, rows):
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |"
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(x).replace("|", r"\|") for x in row) + " |")
    return "\n".join(lines)

disease_names = {
    "diabetes": "Diabetes",
    "heart": "Heart Disease",
    "ckd": "Chronic Kidney Disease",
    "breast_cancer": "Breast Cancer"
}

# Selected model summary: source CSV's Logistic Regression experiment.
selected = comparison[
    comparison["model"].astype(str).str.lower().str.replace("-", "_").str.replace(" ", "_")
    == "logistic_regression"
].copy()

if len(selected) != 4:
    raise SystemExit(
        "Could not verify one Logistic Regression result per disease. "
        "Inspect model_comparison.csv before generating README."
    )

selected_rows = []
for _, r in selected.iterrows():
    selected_rows.append([
        disease_names.get(r["disease"], r["disease"]),
        r["model"],
        fmt_percent(r["accuracy"]),
        fmt_percent(r["precision"]),
        fmt_percent(r["recall"]),
        fmt_percent(r["f1"]),
        fmt_percent(r["roc_auc"])
    ])

# All 24 experiments, with key metrics and supporting experiment metadata.
all_rows = []
for _, r in comparison.sort_values(["disease", "model"]).iterrows():
    all_rows.append([
        disease_names.get(r["disease"], r["disease"]),
        r["model"],
        int(r["dataset_rows"]),
        int(r["train_rows"]),
        int(r["test_rows"]),
        fmt_number(r["cv_roc_auc_mean"]),
        fmt_number(r["cv_roc_auc_std"]),
        fmt_percent(r["accuracy"]),
        fmt_percent(r["precision"]),
        fmt_percent(r["recall"]),
        fmt_percent(r["f1"]),
        fmt_percent(r["roc_auc"]),
        int(r["true_negative"]),
        int(r["false_positive"]),
        int(r["false_negative"]),
        int(r["true_positive"])
    ])

cv_rows = []
for _, r in cv.iterrows():
    cv_rows.append([
        disease_names.get(r["disease"], r["disease"]),
        int(r["rows"]),
        int(r["features"]),
        fmt_percent(r["accuracy_mean"]),
        fmt_percent(r["precision_mean"]),
        fmt_percent(r["recall_mean"]),
        fmt_percent(r["f1_mean"]),
        fmt_percent(r["roc_auc_mean"]),
        fmt_number(r["roc_auc_std"])
    ])

# Use only screenshot files that actually exist in the repository.
screenshots = [
    ("Dashboard", "docs/screenshots/01_MediPredict_AI_Dashboard.png"),
    ("Diabetes Form", "docs/screenshots/02A_MediPredict_AI_Diabetes_Form.png"),
    ("Heart Disease Form", "docs/screenshots/02B_MediPredict_AI_Heart_Disease_Form.png"),
    ("CKD Form", "docs/screenshots/02C_MediPredict_AI_CKD_Form.png"),
    ("Breast Cancer Form", "docs/screenshots/02D_MediPredict_AI_Breast_Cancer_Form.png"),
    ("Prediction Result", "docs/screenshots/03A_MediPredict_AI_Diabetes_Prediction.png"),
    ("Model Analytics", "docs/screenshots/03-model-analytics-circular-performance.png"),
    ("ROC-AUC Analytics", "docs/screenshots/04-model-analytics-roc-auc-comparison.png"),
    ("Saved Assessments", "docs/screenshots/05-reports-saved-assessment.png"),
    ("CSV Export", "docs/screenshots/07-model-evaluation-csv-export.png"),
]

gallery = []
for title, path in screenshots:
    if (ROOT / path).exists():
        gallery.append(
            f'<td width="50%" align="center"><b>{title}</b><br>'
            f'<img src="{path}" alt="{title}" width="100%"></td>'
        )

gallery_html = ""
for i in range(0, len(gallery), 2):
    pair = gallery[i:i+2]
    if len(pair) == 1:
        pair.append("<td width='50%'></td>")
    gallery_html += "<tr>" + "".join(pair) + "</tr>\n"

if not gallery:
    gallery_html = "<tr><td>No screenshot files were found in docs/screenshots/.</td></tr>"

readme = f'''<div align="center">

# MediPredict AI

### AI-Based Multi-Disease Risk Prediction System

**A unified machine learning research platform for four disease prediction workflows.**

<p>
<a href="https://medipredict-ai-two.vercel.app/">
<img src="https://img.shields.io/badge/Live%20Demo-Visit%20Application-2563EB?style=for-the-badge&logo=vercel" alt="Live Demo">
</a>
<a href="https://medipredict-ai-api.onrender.com/api/health">
<img src="https://img.shields.io/badge/API-Health%20Endpoint-16A34A?style=for-the-badge&logo=flask" alt="API">
</a>
<a href="https://github.com/devloperdevesh/ai-multidisease-prediction">
<img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub">
</a>
<a href="LICENSE">
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</a>
</p>

**4 Disease Categories · 6 Algorithms · 24 Model Experiments**

</div>

---

> **Medical disclaimer:** This is an academic machine learning research project. It is not clinically validated and must not be used as a substitute for professional medical advice, diagnosis, or treatment.

## Project at a glance

MediPredict AI combines four disease-specific machine learning workflows with a web application. Users can enter disease-related parameters and receive a model-generated classification through a unified interface.

| Disease category | Prediction task |
|---|---|
| Diabetes | Binary risk classification |
| Heart Disease | Binary risk classification |
| Chronic Kidney Disease (CKD) | Binary classification |
| Breast Cancer | Benign / Malignant classification |

## Application preview

<table>
{gallery_html}
</table>

## Key features

- Unified web interface for four disease workflows.
- Disease-specific input forms and preprocessing.
- Six classification algorithms evaluated per disease.
- 24 recorded model experiments.
- Model performance comparison and analytics.
- Flask REST API integration.
- Saved assessment and evaluation interfaces.
- Automated backend test suite.
- Exportable research evaluation results.

## Model evaluation

The following table shows the Logistic Regression experiment for each disease, based on `reports/results/model_comparison.csv`.

{md_table(
    ["Disease", "Model", "Accuracy", "Precision", "Recall", "F1-Score", "ROC-AUC"],
    selected_rows
)}

**Important:** The selected-model results above are test-set metrics from the recorded experiments. They do not establish clinical performance.

### All 24 model experiments

All experiment records are retained below. Expand this section to inspect the individual algorithms, dataset split sizes, cross-validation ROC-AUC, classification metrics and confusion-matrix counts.

<details>
<summary><b>View complete 24-model comparison table</b></summary>

{md_table(
    ["Disease", "Algorithm", "Dataset Rows", "Train Rows", "Test Rows",
     "CV ROC-AUC Mean", "CV ROC-AUC Std", "Accuracy", "Precision",
     "Recall", "F1", "ROC-AUC", "TN", "FP", "FN", "TP"],
    all_rows
)}

</details>

### Repeated cross-validation audit

The following table is generated from `reports/results/repeated_cv_audit.csv`.

{md_table(
    ["Disease", "Rows", "Features", "Accuracy Mean", "Precision Mean",
     "Recall Mean", "F1 Mean", "ROC-AUC Mean", "ROC-AUC Std"],
    cv_rows
)}

### Evaluation definitions

| Metric | Meaning |
|---|---|
| Accuracy | Overall proportion of correct predictions |
| Precision | Correctness of positive predictions |
| Recall | Ability to identify actual positive cases |
| F1-score | Harmonic mean of precision and recall |
| ROC-AUC | Ability to distinguish between classes |
| Confusion matrix | True negatives, false positives, false negatives and true positives |

### Downloadable experiment evidence

| Resource | Description |
|---|---|
| [Complete Excel evaluation](reports/results/medipredict_model_evaluation.xlsx) | All 24 experiments, CV audit and best-model source |
| [Model comparison CSV](reports/results/model_comparison.csv) | Original experiment metrics |
| [Best models JSON](reports/results/best_models.json) | Selected model records |
| [Detailed evaluation report](docs/MODEL_EVALUATION_EVIDENCE.md) | Expanded research evidence |
| [Dataset audit](reports/results/dataset_audit.json) | Dataset inspection results |
| [Training results](reports/results/model_training_results.json) | Training experiment records |

## Research methodology

1. Dataset acquisition and inspection.
2. Data quality and missing-value assessment.
3. Disease-specific preprocessing.
4. Feature encoding and scaling where required.
5. Training and test split.
6. Six algorithm experiments per disease.
7. Cross-validation and test-set evaluation.
8. Model comparison and selection.
9. Model persistence and API integration.

### Algorithms evaluated

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- XGBoost

## System architecture

```mermaid
flowchart TD
    A[User] --> B[React + Vite Frontend]
    B --> C[Flask REST API]
    C --> D[Input Validation]
    D --> E{{Disease Selection}}
    E --> F[Diabetes]
    E --> G[Heart Disease]
    E --> H[CKD]
    E --> I[Breast Cancer]
    F --> J[Disease-specific Processing]
    G --> J
    H --> J
    I --> J
    J --> K[Trained ML Model]
    K --> L[Prediction Result]
    L --> B
    M[Training and Evaluation Pipeline] --> K
```

## Technology stack

| Layer | Technologies |
|---|---|
| Languages | Python, JavaScript |
| Frontend | React, Vite, HTML, CSS |
| Backend | Flask, REST API |
| Machine Learning | Scikit-learn, XGBoost |
| Data Processing | Pandas, NumPy |
| Model Persistence | Joblib |
| Testing | Pytest |
| Deployment | Vercel, Render |
| Version Control | Git, GitHub |

## Live services

| Component | Link |
|---|---|
| Frontend | [MediPredict AI](https://medipredict-ai-two.vercel.app/) |
| Backend | [Production API](https://medipredict-ai-api.onrender.com) |
| Health endpoint | [API Health](https://medipredict-ai-api.onrender.com/api/health) |
| Source code | [GitHub Repository](https://github.com/devloperdevesh/ai-multidisease-prediction) |

Service availability may vary depending on hosting conditions.

## Local setup

### 1. Clone the repository

```bash
git clone https://github.com/devloperdevesh/ai-multidisease-prediction.git
cd ai-multidisease-prediction
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install frontend dependencies

```bash
npm --prefix frontend install
```

### 5. Start the backend

```bash
python -m app.api.server
```

### 6. Start the frontend in another terminal

```bash
npm --prefix frontend run dev
```

### 7. Run tests

```bash
python -m pytest -q
```

## Repository structure

```text
ai-multidisease-prediction/
├── app/                  # Backend application
├── data/                 # Raw and processed datasets
├── docs/
│   ├── screenshots/     # Application screenshots
│   └── ...              # Research and design documents
├── frontend/             # React + Vite application
├── models/               # Saved disease-specific models
├── reports/
│   └── results/          # Experiment metrics and audits
├── src/                  # Training and ML source code
├── tests/                # Automated tests
├── requirements.txt
├── LICENSE
└── README.md
```

## Project team

| Team Member | Role | Responsibilities |
|---|---|---|
| Devesh Chauhan | Technical Lead | Architecture, backend, integration, ML workflow and technical coordination |
| Karan Kumar Tiwari | UI / Frontend Developer | Interface design and frontend development |
| Payal Chauhan | Research & Presentation | Research and presentation preparation |
| Mamta Tiwari | Research & Documentation | Literature review and academic documentation |

**Project Guide:** Mr. Anurag Gupta, Assistant Professor, Department of Computer Science.

**Institution:** ITS Engineering College, Greater Noida.

**University:** Dr. A.P.J. Abdul Kalam Technical University, Lucknow.

## Limitations and responsible use

- Public benchmark datasets may not represent all patient populations.
- High test-set performance does not establish clinical reliability.
- CKD's unusually high recorded metrics require further leakage, duplicate-record and independent validation checks.
- The project has not undergone independent clinical validation.
- Predictions must not be used for treatment decisions.
- Real-world use requires privacy, security, regulatory and clinical review.

## Future scope

- Independent external dataset validation.
- Explainable AI using SHAP or LIME.
- Model calibration and decision-threshold analysis.
- Dataset provenance and leakage investigation.
- Model monitoring and drift detection.
- Secure and persistent assessment storage.
- Clinical collaboration and validation.

## License

Released under the [MIT License](LICENSE).

---

<div align="center">

**MediPredict AI**

*Machine Learning · Healthcare Research · Full-Stack Engineering*

[Live Demo](https://medipredict-ai-two.vercel.app/) · [GitHub](https://github.com/devloperdevesh/ai-multidisease-prediction)

</div>
'''

(ROOT / "README.md").write_text(readme, encoding="utf-8")

print("README redesigned successfully.")
print("Screenshot images included:", len(gallery))
print("Model experiments included:", len(all_rows))
print("CV audit records included:", len(cv_rows))
print("README size:", (ROOT / "README.md").stat().st_size)
print("Best-model source JSON loaded:", bool(best_json))
