from pydantic import BaseModel, Field


class HospitalCreateRequest(BaseModel):
    hospital_name: str = Field(..., min_length=3, max_length=100)
    hospital_code: str = Field(..., min_length=2, max_length=20)
    location: str = Field(..., min_length=2, max_length=100)
    contact_email: str
    contact_phone: str


class HospitalResponse(BaseModel):
    hospital_id: str
    hospital_name: str
    hospital_code: str
    location: str
    contact_email: str
    contact_phone: str
    status: str