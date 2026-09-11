from fastapi import APIRouter

from schemas.prediction import (
    DiabetesPredictionRequest,
    HeartPredictionRequest,
)

from schemas.auth import VerifyTokenRequest

from services.auth_service import AuthService
from services.prediction_service import PredictionService
from services.history_service import HistoryService

from utils.response import (
    success_response,
    error_response,
)

router = APIRouter()

prediction_service = PredictionService()
history_service = HistoryService()
auth_service = AuthService()


# ---------------------------------------
# Diabetes Prediction
# ---------------------------------------
@router.post("/diabetes")
def predict_diabetes(
    token: VerifyTokenRequest,
    request: DiabetesPredictionRequest,
):
    try:

        user = auth_service.get_current_user(token.id_token)

        result = prediction_service.predict_diabetes(request)

        history_service.save_prediction(
            uid=user["uid"],
            disease="Diabetes",
            prediction=result,
            input_data=request.model_dump(),
        )

        return success_response(
            message="Prediction completed successfully",
            data=result,
        )

    except Exception as e:
        return error_response(
            message=str(e),
            status_code=400,
        )


# ---------------------------------------
# Heart Disease Prediction
# ---------------------------------------
@router.post("/heart")
def predict_heart(
    token: VerifyTokenRequest,
    request: HeartPredictionRequest,
):
    try:

        user = auth_service.get_current_user(token.id_token)

        result = prediction_service.predict_heart(request)

        history_service.save_prediction(
            uid=user["uid"],
            disease="Heart Disease",
            prediction=result,
            input_data=request.model_dump(),
        )

        return success_response(
            message="Prediction completed successfully",
            data=result,
        )

    except Exception as e:
        return error_response(
            message=str(e),
            status_code=400,
        )