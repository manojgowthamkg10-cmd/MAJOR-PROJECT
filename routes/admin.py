from fastapi import APIRouter

from schemas.role import RoleUpdateRequest

from services.role_service import RoleService
from services.admin_service import AdminService

from middleware.admin_auth import verify_admin

from utils.response import (
    success_response,
    error_response,
)


router = APIRouter()


role_service = RoleService()

admin_service = AdminService()



# ======================================================
# Update User Role
# ======================================================

@router.put("/role")
def update_user_role(
    request: RoleUpdateRequest,
    id_token: str
):

    try:

        verify_admin(id_token)


        result = role_service.update_role(
            request.uid,
            request.role
        )


        return success_response(
            message="Role updated successfully",
            data=result
        )


    except Exception as e:

        return error_response(
            message=str(e),
            status_code=400
        )



# ======================================================
# Admin Dashboard
# ======================================================

@router.get("/dashboard")
def admin_dashboard(
    id_token: str
):

    try:

        verify_admin(id_token)


        result = admin_service.get_admin_dashboard()


        return success_response(
            message="Admin dashboard fetched successfully",
            data=result
        )


    except Exception as e:

        return error_response(
            message=str(e),
            status_code=400
        )



# ======================================================
# Users
# ======================================================

@router.get("/users")
def admin_users(
    id_token: str
):

    try:

        verify_admin(id_token)


        result = admin_service.get_user_statistics()


        return success_response(
            message="User statistics fetched successfully",
            data=result
        )


    except Exception as e:

        return error_response(
            message=str(e),
            status_code=400
        )



# ======================================================
# Hospitals
# ======================================================

@router.get("/hospitals")
def admin_hospitals(
    id_token: str
):

    try:

        verify_admin(id_token)


        result = admin_service.get_hospital_statistics()


        return success_response(
            message="Hospital statistics fetched successfully",
            data=result
        )


    except Exception as e:

        return error_response(
            message=str(e),
            status_code=400
        )



# ======================================================
# Predictions
# ======================================================

@router.get("/predictions")
def admin_predictions(
    id_token: str
):

    try:

        verify_admin(id_token)


        result = admin_service.get_prediction_statistics()


        return success_response(
            message="Prediction statistics fetched successfully",
            data=result
        )


    except Exception as e:

        return error_response(
            message=str(e),
            status_code=400
        )



# ======================================================
# Model Status
# ======================================================

@router.get("/model-status")
def model_status(
    id_token: str
):

    try:

        verify_admin(id_token)


        result = admin_service.get_model_status()


        return success_response(
            message="Model status fetched successfully",
            data=result
        )


    except Exception as e:

        return error_response(
            message=str(e),
            status_code=400
        )