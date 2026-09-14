from pathlib import Path
import sys

# Add project root to Python import path.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd

from src.config import RAW_DATA_DIR


PIMA_URL = (
    "https://raw.githubusercontent.com/jbrownlee/Datasets/master/"
    "pima-indians-diabetes.csv"
)

PIMA_COLUMNS = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age",
    "Outcome",
]


def save_dataframe(
    dataframe: pd.DataFrame,
    disease: str,
    filename: str,
) -> Path:

    output_dir = RAW_DATA_DIR / disease
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / filename

    dataframe.to_csv(output_path, index=False)

    return output_path


def download_pima_diabetes() -> Path:

    dataframe = pd.read_csv(PIMA_URL, header=None)

    if dataframe.shape != (768, 9):
        raise ValueError(
            f"Unexpected Pima dataset shape: {dataframe.shape}. "
            "Expected (768, 9)."
        )

    dataframe.columns = PIMA_COLUMNS

    return save_dataframe(
        dataframe,
        "diabetes",
        "pima_diabetes.csv",
    )


def download_uci_dataset(
    dataset_id: int,
    disease: str,
    filename: str,
) -> Path:

    from ucimlrepo import fetch_ucirepo

    dataset = fetch_ucirepo(id=dataset_id)

    features = dataset.data.features.copy()
    targets = dataset.data.targets.copy()

    if targets.shape[1] != 1:
        raise ValueError(
            f"{disease}: expected one target column, "
            f"got {targets.shape[1]}"
        )

    target_name = targets.columns[0]

    dataframe = features.copy()
    dataframe[target_name] = targets.iloc[:, 0]

    if dataframe.empty:
        raise ValueError(
            f"{disease}: downloaded dataset is empty."
        )

    return save_dataframe(
        dataframe,
        disease,
        filename,
    )


def main() -> None:

    print("=" * 60)
    print("DOWNLOADING MULTI-DISEASE DATASETS")
    print("=" * 60)

    print("\n[1/4] Diabetes - Pima Indians")

    diabetes_path = download_pima_diabetes()

    print(f"Saved: {diabetes_path}")

    print("\n[2/4] Heart Disease - UCI")

    heart_path = download_uci_dataset(
        45,
        "heart",
        "uci_heart_disease.csv",
    )

    print(f"Saved: {heart_path}")

    print("\n[3/4] Chronic Kidney Disease - UCI")

    ckd_path = download_uci_dataset(
        336,
        "ckd",
        "uci_chronic_kidney_disease.csv",
    )

    print(f"Saved: {ckd_path}")

    print("\n[4/4] Breast Cancer Wisconsin Diagnostic - UCI")

    breast_path = download_uci_dataset(
        17,
        "breast_cancer",
        "uci_breast_cancer_diagnostic.csv",
    )

    print(f"Saved: {breast_path}")

    print("\n" + "=" * 60)
    print("ALL DATASETS DOWNLOADED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()
