from database.firestore import get_firestore


class PredictionRepository:

    def __init__(self):

        self.db = get_firestore()


    # ==========================================
    # Save Prediction History
    # ==========================================

    def save_prediction(
        self,
        prediction_data: dict
    ):

        doc = (
            self.db
            .collection("prediction_history")
            .document()
        )


        prediction_data["prediction_id"] = doc.id


        doc.set(
            prediction_data
        )


        return prediction_data



    # ==========================================
    # Get All User Predictions
    # Latest Prediction First
    # ==========================================

    def get_user_predictions(
        self,
        uid: str
    ):

        docs = (
            self.db
            .collection("prediction_history")
            .where(
                "uid",
                "==",
                uid
            )
            .order_by(
                "created_at",
                direction="DESCENDING"
            )
            .stream()
        )


        history = []


        for doc in docs:

            history.append(
                doc.to_dict()
            )


        return history



    # ==========================================
    # Get History By Disease
    # Latest Prediction First
    # ==========================================

    def get_predictions_by_disease(
        self,
        uid: str,
        disease: str,
    ):

        docs = (
            self.db
            .collection("prediction_history")
            .where(
                "uid",
                "==",
                uid
            )
            .where(
                "disease",
                "==",
                disease
            )
            .order_by(
                "created_at",
                direction="DESCENDING"
            )
            .stream()
        )


        history = []


        for doc in docs:

            history.append(
                doc.to_dict()
            )


        return history