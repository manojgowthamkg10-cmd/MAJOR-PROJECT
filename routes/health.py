from fastapi import APIRouter

from schemas.auth import VerifyTokenRequest

from services.auth_service import AuthService
from services.health_score_service import HealthScoreService

from utils.response import (
    success_response,
    error_response
)



router = APIRouter()


auth_service = AuthService()

health_service = HealthScoreService()



@router.post("/score")
def calculate_health_score(
    request: VerifyTokenRequest
):

    try:

        user = auth_service.get_current_user(
            request.id_token
        )


        result = health_service.calculate_score(
            user["uid"]
        )


        return success_response(
            message="Health score calculated successfully",
            data=result
        )


    except Exception as e:

        return error_response(
            message=str(e),
            status_code=400
        )