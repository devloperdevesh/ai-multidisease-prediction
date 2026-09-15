import pandas as pd
import pytest

from src.data.preprocessing import (
    normalize_target,
    replace_zero_with_nan,
)
from src.data.dataset import load_training_data
from src.training.config import get_dataset_config
from src.training.split import create_train_test_split


def test_supported_dataset_configs():
    for disease in (
        "diabetes",
        "heart",
        "ckd",
        "breast_cancer",
    ):
        config = get_dataset_config(disease)
        assert config["target"]


def test_invalid_dataset_config():
    with pytest.raises(ValueError):
        get_dataset_config("invalid_disease")


def test_diabetes_zero_values_become_missing():
    dataframe = pd.DataFrame(
        {
            "Glucose": [100, 0],
            "BMI": [25.0, 0.0],
            "Age": [30, 40],
        }
    )

    result = replace_zero_with_nan(
        dataframe,
        ["Glucose", "BMI"],
    )

    assert pd.isna(result.loc[1, "Glucose"])
    assert pd.isna(result.loc[1, "BMI"])
    assert result.loc[1, "Age"] == 40


def test_heart_target_is_binary():
    target = pd.Series([0, 1, 2, 3, 4])

    result = normalize_target(target, "heart")

    assert result.tolist() == [0, 1, 1, 1, 1]


def test_breast_cancer_target_is_binary():
    target = pd.Series(["B", "M", "B", "M"])

    result = normalize_target(target, "breast_cancer")

    assert result.tolist() == [0, 1, 0, 1]


def test_train_test_split_is_stratified_and_reproducible():
    features = pd.DataFrame(
        {
            "feature": range(20),
        }
    )
    target = pd.Series([0, 1] * 10)

    first = create_train_test_split(
        features,
        target,
        test_size=0.2,
    )

    second = create_train_test_split(
        features,
        target,
        test_size=0.2,
    )

    assert first[0].equals(second[0])
    assert first[2].equals(second[2])


@pytest.mark.parametrize(
    "disease",
    ["diabetes", "heart", "ckd", "breast_cancer"],
)
def test_real_dataset_loading(disease):
    features, target = load_training_data(disease)

    assert not features.empty
    assert not target.empty
    assert len(features) == len(target)
    assert set(target.unique()).issubset({0, 1})
