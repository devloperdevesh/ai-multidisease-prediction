from pathlib import Path


# Project root directory
ROOT_DIR = Path(__file__).resolve().parents[1]

# Data directories
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"

# Model and result directories
MODEL_DIR = ROOT_DIR / "models"
RESULTS_DIR = ROOT_DIR / "reports" / "results"


# Supported diseases
DISEASES = [
    "diabetes",
    "heart",
    "ckd",
    "breast_cancer",
]


# Candidate machine learning models
MODEL_NAMES = [
    "logistic_regression",
    "decision_tree",
    "random_forest",
    "svm",
    "knn",
    "xgboost",
]


# Create required directories
for disease in DISEASES:
    (RAW_DATA_DIR / disease).mkdir(parents=True, exist_ok=True)
    (MODEL_DIR / disease).mkdir(parents=True, exist_ok=True)

RESULTS_DIR.mkdir(parents=True, exist_ok=True)
