from pydantic import BaseModel
from typing import Dict, Any


class AdminDashboardResponse(BaseModel):

    users: Dict[str, Any]

    hospitals: Dict[str, Any]

    predictions: Dict[str, Any]

    federated_learning: Dict[str, Any]