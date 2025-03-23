from pydantic import BaseModel, Field
class PassengerData(BaseModel):
    """
    Clase que define el esquema de validación de entrada para la predicción de supervivencia.
    """
    pclass: int = Field(..., ge=1, le=3, description="Clase del pasajero (1, 2, 3)")
    sex: int = Field(..., ge=0, le=1, description="Género (0 = Mujer, 1 = Hombre)")
    age: float = Field(..., gt=0, description="Edad en años")
    sibsp: int = Field(..., ge=0, description="Número de hermanos/esposos a bordo")
    parch: int = Field(..., ge=0, description="Número de padres/hijos a bordo")
    fare: float = Field(..., ge=0, description="Tarifa pagada")
    embarked: int = Field(..., ge=0, le=2, description="Puerto de embarque (0, 1, 2)")

class PredictionResponse(BaseModel):
    """
    Clase que define el esquema de respuesta para la predicción.
    """
    survived: int
