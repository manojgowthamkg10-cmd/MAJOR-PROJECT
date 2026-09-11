import os

from dotenv import load_dotenv


load_dotenv()



class Settings:


    PROJECT_NAME = os.getenv(
        "PROJECT_NAME",
        "Early Detection API"
    )


    VERSION = os.getenv(
        "VERSION",
        "1.0.0"
    )


    HOST = os.getenv(
        "HOST",
        "127.0.0.1"
    )


    PORT = int(
        os.getenv(
            "PORT",
            8000
        )
    )


    FIREBASE_CREDENTIALS = os.getenv(
        "FIREBASE_CREDENTIALS"
    )


    DIABETES_MODEL_PATH = os.getenv(
        "DIABETES_MODEL_PATH"
    )


    DATABASE_NAME = os.getenv(
        "DATABASE_NAME"
    )



settings = Settings()