from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.data.preprocessing import (
    normalize_target,
    replace_zero_with_nan,
    split_features_target,
)
from src.training.config import get_dataset_config


def load_training_data(disease: str) -> tuple[pd.DataFrame, pd.Series]:
    """Load and prepare one disease dataset for model training."""
    config = get_dataset_config(disease)

    dataset_path = Path(config["file"])

    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Dataset not found for '{disease}': {dataset_path}"
        )

    dataframe = pd.read_csv(dataset_path)

    if dataframe.empty:
        raise ValueError(f"Dataset is empty: {dataset_path}")

    dataframe = replace_zero_with_nan(
        dataframe,
        config.get("zero_as_missing", []),
    )

    features, target = split_features_target(
        dataframe,
        config["target"],
    )

    target = normalize_target(target, disease)

    return features, target
