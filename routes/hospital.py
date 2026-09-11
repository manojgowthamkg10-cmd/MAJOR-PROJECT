from fastapi import APIRouter

from schemas.hospital import HospitalCreateRequest
from services.hospital_service import HospitalService
from utils.response import success_response, error_response

router = APIRouter()

hospital_service = HospitalService()


@router.post("/create")
def create_hospital(request: HospitalCreateRequest):
    try:
        result = hospital_service.create_hospital(request)

        return success_response(
            message="Hospital created successfully",
            data=result,
            status_code=201,
        )

    except Exception as e:
        return error_response(
            message=str(e),
            status_code=400,
        )


@router.get("/")
def get_all_hospitals():
    try:
        hospitals = hospital_service.get_all_hospitals()

        return success_response(
            message="Hospitals fetched successfully",
            data=hospitals,
        )

    except Exception as e:
        return error_response(
            message=str(e),
            status_code=400,
        )


@router.get("/{hospital_id}")
def get_hospital(hospital_id: str):
    try:
        hospital = hospital_service.get_hospital(hospital_id)

        return success_response(
            message="Hospital fetched successfully",
            data=hospital,
        )

    except Exception as e:
        return error_response(
            message=str(e),
            status_code=400,
        )