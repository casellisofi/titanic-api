from fastapi import FastAPI, HTTPException
import numpy as np
from app.core.model_loader import load_model 
from app.schemas import PassengerData, PredictionResponse

# -----------------------------------------------------------------------------------
# TITANIC SURVIVAL PREDICTION API
# -----------------------------------------------------------------------------------
# Esta API utiliza un modelo de Machine Learning previamente entrenado (Random Forest)
# para predecir si un pasajero del Titanic habría sobrevivido o no, en base a sus datos.
# -----------------------------------------------------------------------------------

# Inicialización de la aplicación FastAPI con metadatos para documentación automática
app = FastAPI(
    title="Titanic Survival Prediction API",
    description="API para predecir la supervivencia de pasajeros del Titanic usando un modelo de Machine Learning",
    version="1.0",
    openapi_url="/docs/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Cargar el modelo entrenado al iniciar la aplicación
modelo = load_model()

@app.post("/predict/", response_model=PredictionResponse, summary="Realizar predicción de supervivencia")
def predict_survival(data: PassengerData):
    """
    Realiza una predicción sobre la supervivencia del pasajero basándose en sus características.

    ### Campos esperados:
    - **pclass**: Clase del pasajero (1 = Primera, 2 = Segunda, 3 = Tercera)
    - **sex**: Género codificado (0 = Mujer, 1 = Hombre)
    - **age**: Edad del pasajero en años
    - **sibsp**: Número de hermanos/esposos a bordo
    - **parch**: Número de padres/hijos a bordo
    - **fare**: Tarifa pagada por el pasajero
    - **embarked**: Puerto de embarque (0, 1, 2)

    ### Respuesta:
    - **survived**: 1 (Sobrevivió) o 0 (No sobrevivió)
    """
    try:
        # Convertir el input validado en un arreglo NumPy con la estructura requerida por el modelo
        input_data = np.array([[
            data.pclass,
            data.sex,
            data.age,
            data.sibsp,
            data.parch,
            data.fare,
            data.embarked
        ]])

        # Generar la predicción con el modelo cargado
        prediction = modelo.predict(input_data)[0]

        # Retornar la respuesta en formato JSON
        return {"survived": int(prediction)}

    except Exception as e:
        # Manejo de errores internos del modelo o entrada inesperada
        raise HTTPException(status_code=500, detail=f"Error en la predicción: {e}")

@app.get("/", summary="Verificar el estado de la API")
def root():
    """
    Verifica que la API esté operativa.

    ### Respuesta:
    - **message**: Mensaje de confirmación del estado del servicio.
    """
    return {"message": "API de predicción del Titanic funcionando correctamente"}