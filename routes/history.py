from fastapi import APIRouter

from schemas.auth import VerifyTokenRequest

from services.auth_service import AuthService
from services.history_service import HistoryService

from utils.response import (
    success_response,
    error_response,
)

router = APIRouter()

auth_service = AuthService()
history_service = HistoryService()


@router.post("/")
def get_prediction_history(request: VerifyTokenRequest):
    """
    Get all prediction history
    """
    try:
        user = auth_service.get_current_user(request.id_token)

        history = history_service.get_history(
            user["uid"]
        )

        return success_response(
            message="Prediction history fetched successfully",
            data=history,
        )

    except Exception as e:
        return error_response(
            message=str(e),
            status_code=400,
        )


@router.post("/{disease}")
def get_prediction_history_by_disease(
    disease: str,
    request: VerifyTokenRequest,
):
    """
    Get prediction history by disease
    """
    try:
        user = auth_service.get_current_user(request.id_token)

        history = history_service.get_history_by_disease(
            user["uid"],
            disease,
        )

        return success_response(
            message=f"{disease} history fetched successfully",
            data=history,
        )

    except Exception as e:
        return error_response(
            message=str(e),
            status_code=400,
        )