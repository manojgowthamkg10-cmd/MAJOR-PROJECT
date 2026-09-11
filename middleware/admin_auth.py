from fastapi import HTTPException

from services.auth_service import AuthService
from services.role_service import RoleService



auth_service = AuthService()

role_service = RoleService()



def verify_admin(
    id_token: str
):


    try:

        # Verify Firebase token

        user = auth_service.verify_token(
            id_token
        )


        uid = user["uid"]



        # Get user role

        role_data = role_service.get_user_role(
            uid
        )


        role = role_data["role"]



        if role != "ADMIN":

            raise HTTPException(

                status_code=403,

                detail="Admin access required"

            )


        return user



    except HTTPException:

        raise



    except Exception as e:

        raise HTTPException(

            status_code=401,

            detail=str(e)

        )