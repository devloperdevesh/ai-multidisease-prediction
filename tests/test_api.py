import pytest

from app.api.server import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_health(client):
    response = client.get("/api/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert len(data["models_loaded"]) == 4


def test_diseases(client):
    response = client.get("/api/diseases")

    assert response.status_code == 200

    data = response.get_json()

    assert "diseases" in data
    assert len(data["diseases"]) == 4


def test_invalid_disease(client):
    response = client.post(
        "/api/predict/invalid",
        json={},
    )

    assert response.status_code == 404


def test_non_json_request(client):
    response = client.post(
        "/api/predict/diabetes",
        data="invalid",
    )

    assert response.status_code == 400


def test_missing_features(client):
    response = client.post(
        "/api/predict/diabetes",
        json={
            "Glucose": 120
        },
    )

    assert response.status_code == 400

    data = response.get_json()

    assert "missing_features" in data


def test_diabetes_prediction(client):
    payload = {
        "Pregnancies": 2,
        "Glucose": 120,
        "BloodPressure": 70,
        "SkinThickness": 20,
        "Insulin": 80,
        "BMI": 25.0,
        "DiabetesPedigreeFunction": 0.5,
        "Age": 35,
    }

    response = client.post(
        "/api/predict/diabetes",
        json=payload,
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["disease"] == "diabetes"
    assert data["model"]
    assert data["prediction"] in [0, 1]
    assert 0 <= data["risk_percentage"] <= 100
    assert data["risk_level"] in [
        "low",
        "moderate",
        "high",
    ]
    assert "disclaimer" in data
