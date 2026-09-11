from pydantic import BaseModel, Field
from typing import Optional


class ProfileRequest(BaseModel):

    age: int = Field(
        ...,
        gt=0
    )

    gender: str

    height_cm: float = Field(
        ...,
        gt=0
    )

    weight_kg: float = Field(
        ...,
        gt=0
    )


    blood_pressure: str

    blood_sugar: float = Field(
        ...,
        ge=0
    )


    smoking: bool

    alcohol: bool

    exercise_per_week: int = Field(
        ...,
        ge=0
    )



class ProfileResponse(BaseModel):

    uid: str

    age: int

    gender: str

    height_cm: float

    weight_kg: float


    blood_pressure: str

    blood_sugar: float


    smoking: bool

    alcohol: bool

    exercise_per_week: int


    # Health Analytics

    bmi: Optional[float] = None

    bmi_category: Optional[str] = None