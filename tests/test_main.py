import pytest
from fastapi.testclient import TestClient
from app.main import app  

# --------------------------------------------------------------------------------------
# TEST TITANIC SURVIVAL PREDICTION API
# --------------------------------------------------------------------------------------
# Pruebas automatizadas para validar el correcto funcionamiento de la API de predicción
# de supervivencia en el Titanic. Utiliza TestClient de FastAPI y pytest.
# --------------------------------------------------------------------------------------

# Inicializamos el cliente de prueba para interactuar con la API
client = TestClient(app)

# PRUEBAS PARA EL ENDPOINT ROOT #

def test_root_status_ok():
    """
    Test para verificar que el endpoint raíz (/) responde correctamente.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de predicción del Titanic funcionando correctamente"}

# PRUEBAS PARA EL ENDPOINT /predict/ #

@pytest.fixture
def valid_payload():
    """
    Fixture con un JSON válido para prueba de predicción.
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
    Test para verificar que el endpoint /predict/ responde correctamente
    con un JSON válido.
    """
    response = client.post("/predict/", json=valid_payload)
    assert response.status_code == 200
    result = response.json()
    assert "survived" in result
    assert result["survived"] in [0, 1]


def test_predict_invalid_type():
    """
    Test para verificar que se retorna un error 422 cuando el tipo de dato es inválido.
    Ej: 'age' como string en lugar de float.
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
    Test para verificar que se retorna un error 422 cuando un valor está fuera del rango permitido.
    Ej: 'embarked' con un valor inválido.
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
    Test para verificar que se retorna un error 422 cuando falta un campo obligatorio.
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
