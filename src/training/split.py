from __future__ import annotations

import pandas as pd
from sklearn.model_selection import train_test_split

from src.config import RANDOM_STATE


def create_train_test_split(
    features: pd.DataFrame,
    target: pd.Series,
    test_size: float = 0.20,
):
    """Create a reproducible stratified train/test split."""
    if len(features) != len(target):
        raise ValueError("Features and target must contain equal numbers of rows.")

    if not 0 < test_size < 1:
        raise ValueError("test_size must be between 0 and 1.")

    return train_test_split(
        features,
        target,
        test_size=test_size,
        random_state=RANDOM_STATE,
        stratify=target,
    )
