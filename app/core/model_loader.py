import joblib
import os

def load_model():
    """
    Carga el modelo entrenado desde el archivo en 'models/'.
    """
    model_path = os.path.join(os.path.dirname(__file__), '..', '..', 'models', 'modelo_titanic.joblib')
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        raise RuntimeError(f"Error al cargar el modelo: {e}")
