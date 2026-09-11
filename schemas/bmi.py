from pydantic import BaseModel, Field


class BMIRequest(BaseModel):
    """
    Request model for BMI calculation.
    """

    height_cm: float = Field(
        ...,
        gt=0,
        description="Height in centimeters",
        example=183,
    )

    weight_kg: float = Field(
        ...,
        gt=0,
        description="Weight in kilograms",
        example=98,
    )


class BMIResponse(BaseModel):
    """
    Response model for BMI calculation.
    """

    bmi: float
    category: str