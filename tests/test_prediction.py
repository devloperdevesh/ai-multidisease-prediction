import joblib
import pandas as pd
import pytest

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from src.prediction.predictor import Predictor


def create_test_model(path):
    X = pd.DataFrame(
        {
            "feature_1": [1, 2, 3, 4, 5, 6],
            "feature_2": [2, 3, 4, 5, 6, 7],
        }
    )

    y = [0, 0, 0, 1, 1, 1]

    model = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(random_state=42)),
        ]
    )

    model.fit(X, y)
    joblib.dump(model, path)


def test_predictor_loads_model(tmp_path):
    model_path = tmp_path / "model.joblib"

    create_test_model(model_path)

    predictor = Predictor(model_path)

    assert predictor.model is not None


def test_predictor_returns_prediction(tmp_path):
    model_path = tmp_path / "model.joblib"

    create_test_model(model_path)

    predictor = Predictor(model_path)

    features = pd.DataFrame(
        {
            "feature_1": [2],
            "feature_2": [3],
        }
    )

    result = predictor.predict(features)

    assert "prediction" in result
    assert result["prediction"] in [0, 1]


def test_predictor_returns_probability(tmp_path):
    model_path = tmp_path / "model.joblib"

    create_test_model(model_path)

    predictor = Predictor(model_path)

    features = pd.DataFrame(
        {
            "feature_1": [5],
            "feature_2": [6],
        }
    )

    result = predictor.predict(features)

    assert "probability" in result
    assert 0.0 <= result["probability"] <= 1.0


def test_missing_model_fails(tmp_path):
    model_path = tmp_path / "missing_model.joblib"

    with pytest.raises(FileNotFoundError):
        Predictor(model_path)
