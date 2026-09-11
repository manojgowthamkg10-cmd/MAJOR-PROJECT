from fastapi import APIRouter

from schemas.auth import (
    RegisterRequest,
    VerifyTokenRequest,
)

from services.auth_service import AuthService

from utils.response import (
    success_response,
    error_response,
)

router = APIRouter()

auth_service = AuthService()


@router.post("/register")
def register_user(request: RegisterRequest):
    """
    Register a new user.
    """

    try:
        result = auth_service.register_user(request)

        return success_response(
            message=result["message"],
            data=result["user"],
            status_code=201,
        )

    except Exception as e:
        return error_response(
            message=str(e),
            status_code=400,
        )


@router.post("/verify-token")
def verify_token(request: VerifyTokenRequest):
    """
    Verify Firebase ID Token.
    """

    try:
        decoded = auth_service.verify_token(
            request.id_token
        )

        return success_response(
            message="Token verified successfully",
            data=decoded,
        )

    except Exception as e:
        return error_response(
            message=str(e),
            status_code=401,
        )


@router.post("/me")
def get_current_user(request: VerifyTokenRequest):
    """
    Get currently logged-in user.
    """

    try:
        user = auth_service.get_current_user(
            request.id_token
        )

        return success_response(
            message="User fetched successfully",
            data=user,
        )

    except Exception as e:
        return error_response(
            message=str(e),
            status_code=401,
        )