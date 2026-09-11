from fastapi import APIRouter

from services.explanation_service import ExplanationService

from utils.response import success_response



router = APIRouter()

service = ExplanationService()



@router.post("/generate")
def generate_explanation(data: dict):


    result = service.generate_explanation(

        disease=data["disease"],

        probability=data["probability"],

        features=data["features"]

    )


    return success_response(

        message="Explanation generated successfully",

        data=result

    )