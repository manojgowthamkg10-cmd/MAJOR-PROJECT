from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    # -------------------------------------------------
    # Application Information
    # -------------------------------------------------
    APP_NAME: str = "Early Detection of Chronic Diseases API"
    APP_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = True

    # -------------------------------------------------
    # Server Configuration
    # -------------------------------------------------
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    # -------------------------------------------------
    # CORS Configuration
    # -------------------------------------------------
    ALLOWED_ORIGINS: list[str] = Field(
        default=[
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "http://localhost:8080",
            "http://127.0.0.1:8080",
        ]
    )

    # -------------------------------------------------
    # Firebase Admin SDK
    # -------------------------------------------------
    FIREBASE_CREDENTIALS: str = "firebase/firebase_key.json"

    # -------------------------------------------------
    # Firebase Web API Key
    # (Required for Email/Password Login)
    # -------------------------------------------------
    FIREBASE_WEB_API_KEY: str = ""

    # -------------------------------------------------
    # Firestore Configuration
    # -------------------------------------------------
    FIRESTORE_DATABASE: str = "(default)"

    # -------------------------------------------------
    # Login Endpoint
    # -------------------------------------------------
    FIREBASE_LOGIN_URL: str = (
        "https://identitytoolkit.googleapis.com/v1/"
        "accounts:signInWithPassword"
    )

    # -------------------------------------------------
    # Refresh Token Endpoint
    # -------------------------------------------------
    FIREBASE_REFRESH_URL: str = (
        "https://securetoken.googleapis.com/v1/token"
    )

    # -------------------------------------------------
    # Environment Configuration
    # -------------------------------------------------
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns cached application settings.
    """
    return Settings()