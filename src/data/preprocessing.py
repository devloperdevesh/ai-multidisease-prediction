from __future__ import annotations

from typing import Tuple

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def split_features_target(
    dataframe: pd.DataFrame,
    target_column: str,
) -> Tuple[pd.DataFrame, pd.Series]:

    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("dataframe must be a pandas DataFrame")

    if dataframe.empty:
        raise ValueError("Dataset is empty.")

    if target_column not in dataframe.columns:
        raise ValueError(
            f"Target column '{target_column}' not found. "
            f"Available columns: {list(dataframe.columns)}"
        )

    features = dataframe.drop(columns=[target_column])
    target = dataframe[target_column]

    if features.empty:
        raise ValueError(
            "No feature columns remain after removing target."
        )

    if target.isna().all():
        raise ValueError(
            "Target column contains only missing values."
        )

    return features, target


def build_preprocessor(
    features: pd.DataFrame,
) -> ColumnTransformer:

    if not isinstance(features, pd.DataFrame):
        raise TypeError("features must be a pandas DataFrame")

    if features.empty:
        raise ValueError("Feature dataset is empty.")

    numeric_columns = features.select_dtypes(
        include=["number"]
    ).columns.tolist()

    categorical_columns = features.select_dtypes(
        exclude=["number"]
    ).columns.tolist()

    transformers = []

    if numeric_columns:
        numeric_pipeline = Pipeline(
            steps=[
                (
                    "imputer",
                    SimpleImputer(strategy="median"),
                ),
                (
                    "scaler",
                    StandardScaler(),
                ),
            ]
        )

        transformers.append(
            (
                "numeric",
                numeric_pipeline,
                numeric_columns,
            )
        )

    if categorical_columns:
        categorical_pipeline = Pipeline(
            steps=[
                (
                    "imputer",
                    SimpleImputer(strategy="most_frequent"),
                ),
                (
                    "encoder",
                    OneHotEncoder(
                        handle_unknown="ignore",
                    ),
                ),
            ]
        )

        transformers.append(
            (
                "categorical",
                categorical_pipeline,
                categorical_columns,
            )
        )

    if not transformers:
        raise ValueError(
            "Dataset contains no usable feature columns."
        )

    return ColumnTransformer(
        transformers=transformers,
        remainder="drop",
    )
