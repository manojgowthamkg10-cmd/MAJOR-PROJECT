from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=6)
    phone: str
    gender: str
    date_of_birth: str
    height_cm: float
    weight_kg: float


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)


class VerifyTokenRequest(BaseModel):
    id_token: str


class UserResponse(BaseModel):
    uid: str
    full_name: str
    email: EmailStr
    phone: str
    gender: str
    date_of_birth: str
    height_cm: float
    weight_kg: float
    role: str


class MessageResponse(BaseModel):
    message: str