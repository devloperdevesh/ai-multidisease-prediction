from __future__ import annotations

from sklearn.pipeline import Pipeline

from src.data.preprocessing import build_preprocessor
from src.models.model_factory import get_models


def build_model_pipeline(features, model_name: str) -> Pipeline:
    models = get_models()

    if model_name not in models:
        raise ValueError(
            f"Unknown model '{model_name}'. "
            f"Available models: {list(models)}"
        )

    preprocessor = build_preprocessor(features)

    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", models[model_name]),
        ]
    )
