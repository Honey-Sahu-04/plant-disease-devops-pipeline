from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_home_page_loads():
    response = client.get("/")
    assert response.status_code == 200


def test_models_endpoint_returns_available_models():
    response = client.get("/api/models")

    assert response.status_code == 200

    data = response.json()
    assert "models" in data
    assert len(data["models"]) >= 2

    model_ids = {model["id"] for model in data["models"]}
    assert "resnet50" in model_ids
    assert "mobilenet_v2" in model_ids


def test_treatment_endpoint_returns_payload():
    response = client.get("/api/treatment/Tomato___Early_blight")

    assert response.status_code == 200

    data = response.json()
    assert data["available"] is True
    assert data["class_name"] == "Tomato___Early_blight"
    assert "treatment" in data


def test_invalid_model_prediction_fails_cleanly():
    files = {
        "file": ("leaf.jpg", b"not-a-real-image", "image/jpeg"),
    }
    data = {
        "model_name": "invalid_model",
    }

    response = client.post("/api/predict", files=files, data=data)

    assert response.status_code == 400
    assert "Unsupported model" in response.json()["detail"]