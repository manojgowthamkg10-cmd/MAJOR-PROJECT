from datetime import datetime

from firebase_admin import auth

from database.repository import FirestoreRepository

from utils.constants import (
    PATIENT_ROLE,
    USER_REGISTERED,
)

from utils.logger import get_logger


class AuthService:
    """
    Authentication Service
    Handles Firebase Authentication
    and Firestore user operations.
    """

    def __init__(self):
        self.repository = FirestoreRepository()
        self.logger = get_logger()

    def register_user(self, user_data):
        """
        Register a new user.
        """

        # Create Firebase Authentication user
        firebase_user = auth.create_user(
            email=user_data.email,
            password=user_data.password,
        )

        # User document for Firestore
        user_document = {
            "uid": firebase_user.uid,
            "full_name": user_data.full_name,
            "email": user_data.email,
            "phone": user_data.phone,
            "gender": user_data.gender,
            "date_of_birth": user_data.date_of_birth,
            "height_cm": user_data.height_cm,
            "weight_kg": user_data.weight_kg,
            "role": PATIENT_ROLE,
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat(),
        }

        # Save into Firestore
        self.repository.create_user(
            firebase_user.uid,
            user_document,
        )

        self.logger.info(
            f"User Registered: {firebase_user.email}"
        )

        return {
            "message": USER_REGISTERED,
            "user": user_document,
        }

    def verify_token(self, id_token: str):
        """
        Verify Firebase ID Token.
        """

        decoded_token = auth.verify_id_token(id_token)

        self.logger.info(
            f"Token verified for UID: {decoded_token['uid']}"
        )

        return decoded_token

    def get_current_user(self, id_token: str):
        """
        Return currently logged-in user.
        """

        decoded_token = auth.verify_id_token(id_token)

        uid = decoded_token["uid"]

        user = self.repository.get_user_by_uid(uid)

        if not user:
            raise Exception("User not found")

        self.logger.info(
            f"Fetched profile for UID: {uid}"
        )

        return user