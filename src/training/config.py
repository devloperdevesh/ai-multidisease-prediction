from pathlib import Path

from src.config import RAW_DATA_DIR, PROCESSED_DATA_DIR, MODEL_DIR, RESULTS_DIR


DATASET_CONFIG = {
    "diabetes": {
        "file": RAW_DATA_DIR / "diabetes" / "pima_diabetes.csv",
        "target": "Outcome",
        "task": "binary_classification",
        "positive_class": 1,
        "zero_as_missing": [
            "Glucose",
            "BloodPressure",
            "SkinThickness",
            "Insulin",
            "BMI",
        ],
    },
    "heart": {
        "file": RAW_DATA_DIR / "heart" / "uci_heart_disease.csv",
        "target": "num",
        "task": "binary_classification",
        "positive_classes": [1, 2, 3, 4],
        "zero_as_missing": [],
    },
    "ckd": {
        "file": RAW_DATA_DIR / "ckd" / "uci_chronic_kidney_disease.csv",
        "target": "class",
        "task": "binary_classification",
        "positive_class": "ckd",
        "zero_as_missing": [],
    },
    "breast_cancer": {
        "file": (
            RAW_DATA_DIR
            / "breast_cancer"
            / "uci_breast_cancer_diagnostic.csv"
        ),
        "target": "Diagnosis",
        "task": "binary_classification",
        "positive_class": "M",
        "zero_as_missing": [],
    },
}


def get_dataset_config(disease: str) -> dict:
    """Return validated configuration for a supported disease."""
    if disease not in DATASET_CONFIG:
        raise ValueError(
            f"Unsupported disease '{disease}'. "
            f"Supported diseases: {list(DATASET_CONFIG)}"
        )

    return DATASET_CONFIG[disease].copy()


def get_model_output_dir(disease: str) -> Path:
    """Return the model output directory for a disease."""
    path = MODEL_DIR / disease
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_result_output_dir() -> Path:
    """Return the training result directory."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    return RESULTS_DIR


def get_processed_output_dir() -> Path:
    """Return the processed-data directory."""
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    return PROCESSED_DATA_DIR
