from datetime import datetime

from database.firestore import get_firestore
from utils.logger import get_logger



class ProfileService:


    def __init__(self):

        self.db = get_firestore()

        self.logger = get_logger()



    def calculate_bmi(
        self,
        height_cm,
        weight_kg
    ):

        height_m = height_cm / 100

        bmi = round(
            weight_kg / (height_m ** 2),
            2
        )


        if bmi < 18.5:
            category = "Underweight"

        elif bmi < 25:
            category = "Normal"

        elif bmi < 30:
            category = "Overweight"

        else:
            category = "Obesity"


        return bmi, category



    def create_profile(
        self,
        uid: str,
        profile
    ):

        bmi, category = self.calculate_bmi(
            profile.height_cm,
            profile.weight_kg
        )


        profile_data = {

            "uid": uid,

            "age": profile.age,

            "gender": profile.gender,

            "height_cm": profile.height_cm,

            "weight_kg": profile.weight_kg,


            "blood_pressure": profile.blood_pressure,

            "blood_sugar": profile.blood_sugar,


            "smoking": profile.smoking,

            "alcohol": profile.alcohol,

            "exercise_per_week": profile.exercise_per_week,


            "bmi": bmi,

            "bmi_category": category,


            "created_at": datetime.utcnow().isoformat(),

            "updated_at": datetime.utcnow().isoformat(),

        }


        self.db.collection(
            "profiles"
        ).document(uid).set(profile_data)


        self.logger.info(
            f"Profile created for {uid}"
        )


        return profile_data



    def get_profile(
        self,
        uid: str
    ):

        doc = (
            self.db.collection("profiles")
            .document(uid)
            .get()
        )


        if not doc.exists:

            raise Exception(
                "Profile not found"
            )


        return doc.to_dict()



    def update_profile(
        self,
        uid: str,
        profile
    ):

        bmi, category = self.calculate_bmi(
            profile.height_cm,
            profile.weight_kg
        )


        update_data = {

            "age": profile.age,

            "gender": profile.gender,

            "height_cm": profile.height_cm,

            "weight_kg": profile.weight_kg,


            "blood_pressure": profile.blood_pressure,

            "blood_sugar": profile.blood_sugar,


            "smoking": profile.smoking,

            "alcohol": profile.alcohol,

            "exercise_per_week": profile.exercise_per_week,


            "bmi": bmi,

            "bmi_category": category,


            "updated_at": datetime.utcnow().isoformat(),

        }


        self.db.collection(
            "profiles"
        ).document(uid).update(update_data)


        self.logger.info(
            f"Profile updated for {uid}"
        )


        return self.get_profile(uid)