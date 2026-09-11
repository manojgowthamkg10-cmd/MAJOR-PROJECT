from fastapi import APIRouter

from schemas.profile import ProfileRequest
from schemas.auth import VerifyTokenRequest

from services.auth_service import AuthService
from services.profile_service import ProfileService

from utils.response import success_response, error_response

router = APIRouter()

auth_service = AuthService()
profile_service = ProfileService()


@router.post("/create")
def create_profile(
    token: VerifyTokenRequest,
    profile: ProfileRequest,
):
    try:
        user = auth_service.get_current_user(token.id_token)

        result = profile_service.create_profile(
            user["uid"],
            profile,
        )

        return success_response(
            message="Profile created successfully",
            data=result,
            status_code=201,
        )

    except Exception as e:
        return error_response(
            message=str(e),
            status_code=400,
        )


@router.post("/me")
def get_profile(token: VerifyTokenRequest):
    try:
        user = auth_service.get_current_user(token.id_token)

        profile = profile_service.get_profile(user["uid"])

        return success_response(
            message="Profile fetched successfully",
            data=profile,
        )

    except Exception as e:
        return error_response(
            message=str(e),
            status_code=404,
        )


@router.put("/update")
def update_profile(
    token: VerifyTokenRequest,
    profile: ProfileRequest,
):
    try:
        user = auth_service.get_current_user(token.id_token)

        updated = profile_service.update_profile(
            user["uid"],
            profile,
        )

        return success_response(
            message="Profile updated successfully",
            data=updated,
        )

    except Exception as e:
        return error_response(
            message=str(e),
            status_code=400,
        )