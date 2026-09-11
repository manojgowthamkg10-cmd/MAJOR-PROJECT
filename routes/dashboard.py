from fastapi import APIRouter

from schemas.auth import VerifyTokenRequest

from services.auth_service import AuthService
from services.dashboard_service import DashboardService

from utils.response import (
    success_response,
    error_response
)



router = APIRouter()


auth_service = AuthService()

dashboard_service = DashboardService()



@router.post("/")
def get_dashboard(
    request: VerifyTokenRequest
):

    try:

        user = auth_service.get_current_user(
            request.id_token
        )


        dashboard = dashboard_service.get_dashboard(
            user["uid"]
        )


        return success_response(

            message="Dashboard fetched successfully",

            data=dashboard

        )


    except Exception as e:


        return error_response(

            message=str(e),

            status_code=400

        )