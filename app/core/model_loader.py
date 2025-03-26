import joblib
import os

def load_model():
    """
    Loads the trained model from the 'models/' directory.

    Returns:
        **object**: Trained machine learning model.

    Raises:
        **: If loading the model fails.
    """
    model_path = os.path.join(os.path.dirname(__file__), '..', '..', 'models', 'modelo_titanic.joblib')
    try:
        model = joblib.load(model_path)
        return model
    except Exception as e:
        raise RuntimeError(f"Failed to load model: {e}")
