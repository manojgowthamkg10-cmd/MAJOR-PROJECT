import firebase_admin

from firebase_admin import credentials
from firebase_admin import firestore

from config.settings import settings



firebase_app = None



def initialize_firebase():

    global firebase_app


    if firebase_app is None:

        cred = credentials.Certificate(
            settings.FIREBASE_CREDENTIALS
        )


        firebase_app = firebase_admin.initialize_app(
            cred
        )


    return firebase_app



def get_firestore():

    initialize_firebase()

    return firestore.client()