from database.firestore import get_firestore
from utils.constants import PATIENT_ROLE


class AdminService:

    def __init__(self):
        self.db = get_firestore()


    # ==========================================
    # User Statistics
    # ==========================================

    def get_user_statistics(self):

        users = self.db.collection("users").stream()

        total_users = 0
        patients = 0
        doctors = 0
        hospitals = 0
        admins = 0


        for user in users:

            total_users += 1

            role = user.to_dict().get(
                "role",
                PATIENT_ROLE
            )


            if role == "PATIENT":
                patients += 1

            elif role == "DOCTOR":
                doctors += 1

            elif role == "HOSPITAL":
                hospitals += 1

            elif role == "ADMIN":
                admins += 1


        return {

            "total_users": total_users,

            "patients": patients,

            "doctors": doctors,

            "hospitals": hospitals,

            "admins": admins

        }


    # ==========================================
    # Hospital Statistics
    # ==========================================

    def get_hospital_statistics(self):

        hospitals = self.db.collection(
            "hospitals"
        ).stream()


        total = 0


        for hospital in hospitals:
            total += 1


        return {

            "total_hospitals": total,

            "status": "ACTIVE"

        }


    # ==========================================
    # Prediction Statistics
    # ==========================================

    def get_prediction_statistics(self):

        predictions = self.db.collection(
            "prediction_history"
        ).stream()


        total = 0
        diabetes = 0
        heart = 0
        high_risk = 0


        for prediction in predictions:

            data = prediction.to_dict()

            total += 1


            if data.get("disease") == "Diabetes":
                diabetes += 1


            elif data.get("disease") == "Heart Disease":
                heart += 1


            if data.get(
                "probability",
                0
            ) >= 80:

                high_risk += 1



        return {

            "total_predictions": total,

            "diabetes_predictions": diabetes,

            "heart_predictions": heart,

            "high_risk_cases": high_risk

        }



    # ==========================================
    # Federated Model Status
    # ==========================================

    def get_model_status(self):

        return {

            "model":
            "diabetes_global.keras",

            "training_rounds":
            3,

            "clients":
            3,

            "status":
            "ACTIVE"

        }



    # ==========================================
    # Complete Admin Dashboard
    # ==========================================

    def get_admin_dashboard(self):

        return {

            "users":
            self.get_user_statistics(),

            "hospitals":
            self.get_hospital_statistics(),

            "predictions":
            self.get_prediction_statistics(),

            "federated_learning":
            self.get_model_status()

        }