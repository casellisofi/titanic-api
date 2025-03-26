import numpy as np
from app.schemas import PassengerData

def convert_passenger_to_array(data: PassengerData) -> np.ndarray:
    """
    Converts a PassengerData object into a NumPy array formatted for model prediction.

    Args:
        **data (PassengerData)**: The input passenger data.

    Returns:
        **np.ndarray**: A 2D array of shape (1, 7) with passenger features.
    """
    return np.array([[data.pclass, data.sex, data.age, data.sibsp, data.parch, data.fare, data.embarked]])
