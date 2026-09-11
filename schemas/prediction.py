from pydantic import BaseModel, Field
from typing import List, Optional


# ---------------------------------
# Diabetes Prediction Request
# ---------------------------------
class DiabetesPredictionRequest(BaseModel):

    pregnancies: int = Field(..., ge=0)
    glucose: float = Field(..., ge=0)
    blood_pressure: float = Field(..., ge=0)
    skin_thickness: float = Field(..., ge=0)
    insulin: float = Field(..., ge=0)
    bmi: float = Field(..., ge=0)
    diabetes_pedigree_function: float = Field(..., ge=0)
    age: int = Field(..., ge=0)



# ---------------------------------
# Heart Disease Prediction Request
# ---------------------------------
class HeartPredictionRequest(BaseModel):

    age: int = Field(..., ge=1)
    sex: int = Field(..., ge=0, le=1)
    cp: int = Field(..., ge=0, le=3)
    trestbps: float = Field(..., ge=0)
    chol: float = Field(..., ge=0)
    fbs: int = Field(..., ge=0, le=1)
    restecg: int = Field(..., ge=0, le=2)
    thalach: float = Field(..., ge=0)
    exang: int = Field(..., ge=0, le=1)
    oldpeak: float = Field(..., ge=0)
    slope: int = Field(..., ge=0, le=2)
    ca: int = Field(..., ge=0, le=4)
    thal: int = Field(..., ge=0, le=3)


# ---------------------------------
# Common Prediction Response
# ---------------------------------

class PredictionResponse(BaseModel):

    disease: str

    prediction: str

    probability: float

    # AI Healthcare Enhancements

    risk_level: Optional[str] = None

    confidence_score: Optional[float] = None

    # Explainable AI

    contributing_factors: Optional[List[str]] = None

    # Personalized guidance

    recommendations: Optional[List[str]] = None

    health_tips: Optional[List[str]] = None

    disclaimer: Optional[str] = (
        "This prediction is AI-assisted and "
        "not a medical diagnosis. Please consult "
        "a healthcare professional."
    )