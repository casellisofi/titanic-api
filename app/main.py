from fastapi import FastAPI, HTTPException
import numpy as np
from app.core.model_loader import load_model 
from app.schemas import PassengerData, PredictionResponse
from app.utils.preprocessing import convert_passenger_to_array

# -----------------------------------------------------------------------------------
# TITANIC SURVIVAL PREDICTION API
# -----------------------------------------------------------------------------------
# Esta API utiliza un modelo de Machine Learning previamente entrenado (Random Forest)
# para predecir si un pasajero del Titanic habría sobrevivido o no, en base a sus datos.
# -----------------------------------------------------------------------------------

app = FastAPI(
    title="Titanic Survival Prediction API",
    description="API to predict Titanic passenger survival using a trained Machine Learning model",
    version="1.0",
    openapi_url="/docs/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

modelo = load_model()

@app.post("/predict/", response_model=PredictionResponse, summary="Predict passenger survival")
def predict_survival(data: PassengerData):
    """
    Predict whether a Titanic passenger would have survived based on their personal features.

    Args:
        **data (PassengerData)**: Passenger input including class, gender, age, family info, fare and embarkation port.

    Returns:
        **dict**: A JSON object with the survival prediction (1 or 0).

    Raises:
        **HTTPException**: 500 if an internal error occurs during prediction.
    """
    try:
        input_data = convert_passenger_to_array(data)
        prediction = modelo.predict(input_data)[0]
        return {"survived": int(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")

@app.get("/", summary="Check API health status")
def root():
    """
    Health check endpoint to verify the API is operational.

    Returns:
        **dict**: A confirmation message with status.
    """
    return {"message": "Titanic prediction API is up and running"}
