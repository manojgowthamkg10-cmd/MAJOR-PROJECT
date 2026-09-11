from pydantic import BaseModel
from typing import List, Dict


class HealthScoreResponse(BaseModel):

    health_score: float

    status: str

    factors: Dict[str, float]

    recommendations: List[str]