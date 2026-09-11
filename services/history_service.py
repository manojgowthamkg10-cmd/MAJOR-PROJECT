from datetime import datetime

from database.prediction_repository import PredictionRepository


class HistoryService:

    def __init__(self):

        self.repository = PredictionRepository()


    # ==========================================
    # Save Prediction Result
    # ==========================================

    def save_prediction(
        self,
        uid: str,
        disease: str,
        prediction: dict,
        input_data: dict,
    ):

        prediction_data = {

            "uid": uid,

            "disease": disease,


            # Basic prediction
            "prediction": prediction.get(
                "prediction"
            ),

            "probability": prediction.get(
                "probability"
            ),


            # AI Enhanced Data

            "risk_level": prediction.get(
                "risk_level"
            ),

            "confidence_score": prediction.get(
                "confidence_score"
            ),


            # Explainable AI

            "contributing_factors": prediction.get(
                "contributing_factors",
                []
            ),


            # Recommendations

            "recommendations": prediction.get(
                "recommendations",
                []
            ),


            "health_tips": prediction.get(
                "health_tips",
                []
            ),


            # User Input

            "input_features": input_data,


            "created_at": datetime.utcnow().isoformat(),

        }


        return self.repository.save_prediction(
            prediction_data
        )


    # ==========================================
    # Get All History
    # ==========================================

    def get_history(
        self,
        uid: str
    ):

        return self.repository.get_user_predictions(
            uid
        )


    # ==========================================
    # Get Disease Specific History
    # ==========================================

    def get_history_by_disease(
        self,
        uid: str,
        disease: str,
    ):

        return self.repository.get_predictions_by_disease(
            uid,
            disease,
        )