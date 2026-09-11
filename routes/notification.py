from fastapi import APIRouter

from schemas.auth import VerifyTokenRequest

from services.auth_service import AuthService
from services.notification_service import NotificationService

from utils.response import (
    success_response,
    error_response
)


router = APIRouter()


auth_service = AuthService()

notification_service = NotificationService()



@router.post("/")
def get_notifications(
    request: VerifyTokenRequest
):

    try:

        user = auth_service.get_current_user(
            request.id_token
        )


        notifications = (
            notification_service
            .get_notifications(
                user["uid"]
            )
        )


        return success_response(

            message="Notifications fetched successfully",

            data=notifications

        )


    except Exception as e:


        return error_response(

            message=str(e),

            status_code=400

        )