from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import joblib
import pandas as pd

from src.config import MODEL_DIR, RESULTS_DIR, DISEASES


class ProductionPredictor:
    """
    Loads the selected production model for a disease and performs
    prediction using the complete persisted preprocessing + model pipeline.
    """

    def __init__(self, disease: str):
        if disease not in DISEASES:
            raise ValueError(
                f"Unsupported disease: {disease}. "
                f"Available: {list(DISEASES)}"
            )

        self.disease = disease

        best_models_path = RESULTS_DIR / "best_models.json"

        if not best_models_path.exists():
            raise FileNotFoundError(
                f"Best-model registry not found: {best_models_path}"
            )

        with best_models_path.open(
            "r",
            encoding="utf-8",
        ) as file:
            registry = json.load(file)

        if disease not in registry:
            raise ValueError(
                f"No production model registered for '{disease}'."
            )

        self.model_name = registry[disease]["model"]

        model_path = MODEL_DIR / disease / f"{self.model_name}.joblib"

        if not model_path.exists():
            raise FileNotFoundError(
                f"Production model artifact not found: {model_path}"
            )

        self.model_path = model_path
        self.model = joblib.load(model_path)

    def predict(self, features: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(features, dict):
            raise TypeError(
                "features must be a dictionary."
            )

        if not features:
            raise ValueError(
                "Prediction input cannot be empty."
            )

        dataframe = pd.DataFrame([features])

        prediction = self.model.predict(dataframe)

        if len(prediction) != 1:
            raise ValueError(
                "Model returned an invalid prediction."
            )

        predicted_class = int(prediction[0])

        probability = None

        if hasattr(self.model, "predict_proba"):
            probabilities = self.model.predict_proba(dataframe)

            if probabilities.shape[1] == 2:
                probability = float(
                    probabilities[0][1]
                )

        return {
            "disease": self.disease,
            "model": self.model_name,
            "prediction": predicted_class,
            "risk_probability": probability,
            "risk_percentage": (
                round(probability * 100, 2)
                if probability is not None
                else None
            ),
        }
