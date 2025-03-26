import pytest
from fastapi.testclient import TestClient
from app.main import app  

client = TestClient(app)

# ------------------------ ROOT ENDPOINT TEST ------------------------

def test_root_status_ok():
    """
    Test to ensure the root ("/") endpoint is reachable and returns expected message.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Titanic prediction API is up and running"}

# ------------------------ /predict/ ENDPOINT TESTS ------------------------

@pytest.fixture
def valid_payload():
    """
    Fixture returning a valid input payload for Titanic prediction.
    """
    return {
        "pclass": 3,
        "sex": 1,
        "age": 22.0,
        "sibsp": 1,
        "parch": 0,
        "fare": 7.25,
        "embarked": 0
    }

def test_predict_valid_input(valid_payload):
    """
    Test that a valid input returns a 200 OK and a valid prediction (0 or 1).
    """
    response = client.post("/predict/", json=valid_payload)
    assert response.status_code == 200
    result = response.json()
    assert "survived" in result
    assert result["survived"] in [0, 1]

def test_predict_invalid_type():
    """
    Test for 422 error when a field has incorrect data type (e.g. 'age' as string).
    """
    payload = {
        "pclass": 3,
        "sex": 1,
        "age": "twenty",
        "sibsp": 1,
        "parch": 0,
        "fare": 7.25,
        "embarked": 0
    }
    response = client.post("/predict/", json=payload)
    assert response.status_code == 422

def test_predict_out_of_range():
    """
    Test for 422 error when a field is outside its valid range (e.g. 'embarked' too large).
    """
    payload = {
        "pclass": 3,
        "sex": 1,
        "age": 22.0,
        "sibsp": 1,
        "parch": 0,
        "fare": 7.25,
        "embarked": 99
    }
    response = client.post("/predict/", json=payload)
    assert response.status_code == 422

def test_predict_missing_field():
    """
    Test for 422 error when a required field is missing (e.g. 'fare').
    """
    payload = {
        "pclass": 3,
        "sex": 1,
        "age": 22.0,
        "sibsp": 1,
        "parch": 0,
        "embarked": 0
    }
    response = client.post("/predict/", json=payload)
    assert response.status_code == 422
