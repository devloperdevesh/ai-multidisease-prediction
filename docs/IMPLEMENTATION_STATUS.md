# Implementation Status and Evidence Boundaries

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
