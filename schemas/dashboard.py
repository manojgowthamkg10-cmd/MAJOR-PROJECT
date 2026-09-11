from pydantic import BaseModel
from typing import List, Dict, Any


class DashboardResponse(BaseModel):

    user_profile: Dict[str, Any]

    bmi: Dict[str, Any]

    health_score: Dict[str, Any]

    recent_predictions: List[Dict[str, Any]]

    risk_summary: str