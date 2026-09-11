from firebase.firebase_admin import db


def get_firestore():
    """
    Return Firestore client.
    """
    return db