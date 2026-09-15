import pandas as pd
import pytest

from src.training.pipeline import build_model_pipeline
from src.training.train_all import evaluate_predictions


def test_build_model_pipeline():
    features = pd.DataFrame(
        {
            "age": [20, 30, 40, 50],
            "value": [1.0, 2.0, 3.0, 4.0],
        }
    )

    pipeline = build_model_pipeline(
        features,
        "logistic_regression",
    )

    assert "preprocessor" in pipeline.named_steps
    assert "classifier" in pipeline.named_steps


def test_invalid_model_name():
    features = pd.DataFrame(
        {
            "age": [20, 30],
            "value": [1.0, 2.0],
        }
    )

    with pytest.raises(ValueError):
        build_model_pipeline(
            features,
            "invalid_model",
        )


def test_evaluate_predictions():
    from sklearn.linear_model import LogisticRegression

    model = LogisticRegression()

    x_train = pd.DataFrame(
        {
            "x": [0, 1, 0, 1, 0, 1],
        }
    )

    y_train = pd.Series(
        [0, 1, 0, 1, 0, 1]
    )

    model.fit(x_train, y_train)

    metrics = evaluate_predictions(
        model,
        x_train,
        y_train,
    )

    assert "accuracy" in metrics
    assert "precision" in metrics
    assert "recall" in metrics
    assert "f1" in metrics
    assert "roc_auc" in metrics
    assert 0 <= metrics["accuracy"] <= 1
    assert 0 <= metrics["roc_auc"] <= 1
