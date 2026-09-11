from fastapi import APIRouter

from schemas.bmi import BMIRequest

from services.bmi_service import BMIService

from utils.response import (
    success_response,
    error_response,
)


router = APIRouter()

bmi_service = BMIService()



# ==========================================
# Calculate BMI
# ==========================================

@router.post("/calculate")
def calculate_bmi(
    request: BMIRequest
):

    try:

        result = bmi_service.calculate_bmi(
            height_cm=request.height_cm,
            weight_kg=request.weight_kg,
        )


        return success_response(
            message="BMI calculated successfully",
            data=result,
        )


    except Exception as e:

        return error_response(
            message=str(e),
            status_code=400,
        )