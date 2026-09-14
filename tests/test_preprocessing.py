import pandas as pd
import pytest

from src.data.preprocessing import (
    split_features_target,
    build_preprocessor,
)


def sample_dataframe():
    return pd.DataFrame(
        {
            "age": [20, 30, 40, 50],
            "glucose": [90, 120, 150, 180],
            "gender": ["M", "F", "M", "F"],
            "target": [0, 1, 1, 0],
        }
    )


def test_split_features_target():
    dataframe = sample_dataframe()

    X, y = split_features_target(dataframe, "target")

    assert "target" not in X.columns
    assert list(X.columns) == ["age", "glucose", "gender"]
    assert len(X) == len(y) == 4


def test_split_features_target_invalid_column():
    dataframe = sample_dataframe()

    with pytest.raises(ValueError):
        split_features_target(dataframe, "does_not_exist")


def test_preprocessor_creation():
    dataframe = sample_dataframe()
    X, _ = split_features_target(dataframe, "target")

    preprocessor = build_preprocessor(X)

    assert preprocessor is not None
    assert hasattr(preprocessor, "fit")
    assert hasattr(preprocessor, "transform")


def test_preprocessor_handles_numeric_and_categorical_data():
    dataframe = sample_dataframe()
    X, _ = split_features_target(dataframe, "target")

    preprocessor = build_preprocessor(X)

    transformed = preprocessor.fit_transform(X)

    assert transformed.shape[0] == len(X)
    assert transformed.shape[1] > 0


def test_empty_feature_dataset_fails():
    dataframe = pd.DataFrame({"target": [0, 1, 0]})

    with pytest.raises(ValueError):
        split_features_target(dataframe, "target")
