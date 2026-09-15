from __future__ import annotations

from flask import Flask, jsonify, request

from src.config import DISEASES
from src.prediction.production_predictor import ProductionPredictor
from src.prediction.schemas import get_disease_schema


def create_app() -> Flask:
    app = Flask(__name__)

    predictors = {
        disease: ProductionPredictor(disease)
        for disease in DISEASES
    }

    @app.get("/api/health")
    def health():
        return jsonify(
            {
                "status": "healthy",
                "service": "MediPredict AI API",
                "models_loaded": list(predictors.keys()),
            }
        )

    @app.get("/api/diseases")
    def diseases():
        result = []

        for disease in DISEASES:
            schema = get_disease_schema(disease)

            result.append(
                {
                    "id": disease,
                    "label": schema["label"],
                    "feature_count": len(
                        schema["features"]
                    ),
                    "features": schema["features"],
                    "model": predictors[disease].model_name,
                }
            )

        return jsonify(
            {
                "diseases": result
            }
        )

    @app.post("/api/predict/<disease>")
    def predict(disease: str):
        if disease not in predictors:
            return jsonify(
                {
                    "error": "Unsupported disease",
                    "available_diseases": list(
                        predictors.keys()
                    ),
                }
            ), 404

        if not request.is_json:
            return jsonify(
                {
                    "error": "Request must contain JSON."
                }
            ), 400

        payload = request.get_json(silent=True)

        if not isinstance(payload, dict):
            return jsonify(
                {
                    "error": "JSON body must be an object."
                }
            ), 400

        try:
            schema = get_disease_schema(disease)

            missing = [
                feature
                for feature in schema["features"]
                if feature not in payload
            ]

            if missing:
                return jsonify(
                    {
                        "error": "Missing required features.",
                        "missing_features": missing,
                    }
                ), 400

            features = {
                feature: payload[feature]
                for feature in schema["features"]
            }

            result = predictors[disease].predict(
                features
            )

            risk_percentage = result.get(
                "risk_percentage"
            )

            if risk_percentage is not None:
                if risk_percentage >= 70:
                    risk_level = "high"
                elif risk_percentage >= 40:
                    risk_level = "moderate"
                else:
                    risk_level = "low"
            else:
                risk_level = "unknown"

            result["risk_level"] = risk_level

            result["disclaimer"] = (
                "This system provides preliminary risk "
                "prediction for research and educational "
                "purposes only. It is not a medical diagnosis "
                "and should not replace professional medical advice."
            )

            return jsonify(result)

        except (TypeError, ValueError) as exc:
            return jsonify(
                {
                    "error": str(exc)
                }
            ), 400

        except Exception:
            app.logger.exception(
                "Prediction failed for %s",
                disease,
            )

            return jsonify(
                {
                    "error": (
                        "Prediction service encountered "
                        "an unexpected error."
                    )
                }
            ), 500

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
    )
