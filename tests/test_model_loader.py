import pytest
import os
from app.core.model_loader import load_model

def test_load_model_success():
    """
    Test successful model loading when the model file exists.
    """
    model = load_model()
    assert model is not None 

def test_load_model_failure(monkeypatch):
    """
    Simulate model loading failure and expect RuntimeError.
    """
    fake_path = os.path.join(os.path.dirname(__file__), 'non_existing_model.joblib')

    monkeypatch.setattr("app.core.model_loader.os.path.join", lambda *args: fake_path)

    with pytest.raises(RuntimeError) as exc_info:
        load_model()

    assert "Failed to load model" in str(exc_info.value)
