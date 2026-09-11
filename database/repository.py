from database.firestore import get_firestore

from utils.constants import USERS_COLLECTION


class FirestoreRepository:
    """
    Repository layer for Firestore operations.
    """

    def __init__(self):
        self.db = get_firestore()

    # ----------------------------------------
    # Create User
    # ----------------------------------------
    def create_user(self, uid: str, user_data: dict):
        self.db.collection(
            USERS_COLLECTION
        ).document(uid).set(user_data)

    # ----------------------------------------
    # Get User
    # ----------------------------------------
    def get_user_by_uid(self, uid: str):
        document = (
            self.db.collection(USERS_COLLECTION)
            .document(uid)
            .get()
        )

        if document.exists:
            return document.to_dict()

        return None

    # ----------------------------------------
    # Update User
    # ----------------------------------------
    def update_user(self, uid: str, data: dict):
        self.db.collection(
            USERS_COLLECTION
        ).document(uid).update(data)

    # ----------------------------------------
    # Delete User
    # ----------------------------------------
    def delete_user(self, uid: str):
        self.db.collection(
            USERS_COLLECTION
        ).document(uid).delete()

    # ----------------------------------------
    # Check User Exists
    # ----------------------------------------
    def user_exists(self, uid: str) -> bool:
        document = (
            self.db.collection(USERS_COLLECTION)
            .document(uid)
            .get()
        )

        return document.exists