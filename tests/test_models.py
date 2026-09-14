from src.models.model_factory import get_models


def test_all_required_models_exist():
    models = get_models()

    expected_models = {
        "logistic_regression",
        "decision_tree",
        "random_forest",
        "svm",
        "knn",
        "xgboost",
    }

    assert set(models.keys()) == expected_models


def test_model_instances_are_created():
    models = get_models()

    assert len(models) == 6

    for name, model in models.items():
        assert model is not None
        assert hasattr(model, "fit")
        assert hasattr(model, "predict")


def test_models_have_unique_names():
    models = get_models()

    assert len(models.keys()) == len(set(models.keys()))
