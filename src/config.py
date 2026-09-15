from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODEL_DIR = PROJECT_ROOT / "models"
RESULTS_DIR = PROJECT_ROOT / "reports" / "results"

DISEASES = (
    "diabetes",
    "heart",
    "ckd",
    "breast_cancer",
)

MODEL_NAMES = (
    "logistic_regression",
    "decision_tree",
    "random_forest",
    "svm",
    "knn",
    "xgboost",
)

RANDOM_STATE = 42

for disease in DISEASES:
    (RAW_DATA_DIR / disease).mkdir(parents=True, exist_ok=True)
    (MODEL_DIR / disease).mkdir(parents=True, exist_ok=True)

PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
