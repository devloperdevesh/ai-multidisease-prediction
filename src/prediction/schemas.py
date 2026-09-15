from __future__ import annotations


DISEASE_SCHEMAS = {
    "diabetes": {
        "label": "Diabetes",
        "features": [
            "Pregnancies",
            "Glucose",
            "BloodPressure",
            "SkinThickness",
            "Insulin",
            "BMI",
            "DiabetesPedigreeFunction",
            "Age",
        ],
    },

    "heart": {
        "label": "Heart Disease",
        "features": [
            "age",
            "sex",
            "cp",
            "trestbps",
            "chol",
            "fbs",
            "restecg",
            "thalach",
            "exang",
            "oldpeak",
            "slope",
            "ca",
            "thal",
        ],
    },

    "ckd": {
        "label": "Chronic Kidney Disease",
        "features": [
            "age",
            "bp",
            "sg",
            "al",
            "su",
            "rbc",
            "pc",
            "pcc",
            "ba",
            "bgr",
            "bu",
            "sc",
            "sod",
            "pot",
            "hemo",
            "pcv",
            "wbcc",
            "rbcc",
            "htn",
            "dm",
            "cad",
            "appet",
            "pe",
            "ane",
        ],
    },

    "breast_cancer": {
        "label": "Breast Cancer",
        "features": [
            "radius1",
            "texture1",
            "perimeter1",
            "area1",
            "smoothness1",
            "compactness1",
            "concavity1",
            "concave_points1",
            "symmetry1",
            "fractal_dimension1",
            "radius2",
            "texture2",
            "perimeter2",
            "area2",
            "smoothness2",
            "compactness2",
            "concavity2",
            "concave_points2",
            "symmetry2",
            "fractal_dimension2",
            "radius3",
            "texture3",
            "perimeter3",
            "area3",
            "smoothness3",
            "compactness3",
            "concavity3",
            "concave_points3",
            "symmetry3",
            "fractal_dimension3",
        ],
    },
}


def get_disease_schema(disease: str) -> dict:
    if disease not in DISEASE_SCHEMAS:
        raise ValueError(
            f"Unsupported disease: {disease}"
        )

    return DISEASE_SCHEMAS[disease].copy()
