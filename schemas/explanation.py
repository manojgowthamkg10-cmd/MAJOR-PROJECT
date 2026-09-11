from pydantic import BaseModel
from typing import List


class ExplanationResponse(BaseModel):

    disease: str

    risk_level: str

    explanation: str

    risk_factors: List[str]

    recommendations: List[str]