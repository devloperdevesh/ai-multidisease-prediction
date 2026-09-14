from __future__ import annotations

from pathlib import Path
from typing import Any

import joblib


class Predictor:

    def __init__(self, model_path: Path):

        self.model_path = Path(model_path)

        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Model artifact not found: {self.model_path}"
            )

        self.model = joblib.load(self.model_path)

    def predict(self, features: Any) -> dict:

        prediction = self.model.predict(features)

        if len(prediction) == 0:
            raise ValueError(
                "Model returned an empty prediction."
            )

        result = {
            "prediction": prediction[0]
        }

        if hasattr(self.model, "predict_proba"):

            probabilities = self.model.predict_proba(features)

            if probabilities.shape[1] == 2:

                result["probability"] = float(
                    probabilities[0][1]
                )

        return result
