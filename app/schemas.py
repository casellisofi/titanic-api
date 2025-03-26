from pydantic import BaseModel, Field

class PassengerData(BaseModel):
    """
    Input schema for Titanic passenger prediction.
    """
    pclass: int = Field(..., ge=1, le=3, description="Passenger class (1, 2, 3)")
    sex: int = Field(..., ge=0, le=1, description="Gender (0 = Female, 1 = Male)")
    age: float = Field(..., gt=0, description="Passenger age in years")
    sibsp: int = Field(..., ge=0, description="Number of siblings/spouses aboard")
    parch: int = Field(..., ge=0, description="Number of parents/children aboard")
    fare: float = Field(..., ge=0, description="Fare paid by the passenger")
    embarked: int = Field(..., ge=0, le=2, description="Port of embarkation (0, 1, 2)")

class PredictionResponse(BaseModel):
    """
    Output schema for Titanic prediction.
    """
    survived: int
