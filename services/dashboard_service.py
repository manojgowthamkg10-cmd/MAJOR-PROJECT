from services.profile_service import ProfileService
from services.history_service import HistoryService
from services.bmi_service import BMIService


class DashboardService:


    def __init__(self):

        self.profile_service = ProfileService()

        self.history_service = HistoryService()



    def get_dashboard(self, uid):


        # -------------------------
        # Profile
        # -------------------------

        profile = self.profile_service.get_profile(uid)



        # -------------------------
        # BMI
        # -------------------------

        bmi = BMIService.calculate_bmi(

            profile["height_cm"],

            profile["weight_kg"]

        )



        # -------------------------
        # Prediction History
        # -------------------------

        history = self.history_service.get_history(uid)


        recent_predictions = history[-5:]



        # -------------------------
        # Risk Summary
        # -------------------------

        risk_summary = (
            "Your health status is stable."
        )


        for prediction in recent_predictions:


            if prediction.get("probability", 0) >= 80:


                risk_summary = (

                    "High health risk detected. "
                    "Medical monitoring recommended."

                )

                break



        return {


            "user_profile": profile,


            "bmi": bmi,


            "recent_predictions": recent_predictions,


            "risk_summary": risk_summary

        }