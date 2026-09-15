import pytest

from src.prediction.production_predictor import ProductionPredictor
from src.prediction.schemas import get_disease_schema


@pytest.mark.parametrize(
    "disease",
    [
        "diabetes",
        "heart",
        "ckd",
        "breast_cancer",
    ],
)
def test_production_model_loads(disease):
    predictor = ProductionPredictor(disease)

    assert predictor.disease == disease
    assert predictor.model_name
    assert predictor.model is not None
    assert predictor.model_path.exists()


@pytest.mark.parametrize(
    "disease",
    [
        "diabetes",
        "heart",
        "ckd",
        "breast_cancer",
    ],
)
def test_schema_exists(disease):
    schema = get_disease_schema(disease)

    assert schema["label"]
    assert len(schema["features"]) > 0


def test_invalid_disease_predictor():
    with pytest.raises(ValueError):
        ProductionPredictor("invalid_disease")


def test_invalid_disease_schema():
    with pytest.raises(ValueError):
        get_disease_schema("invalid_disease")
