import os

import numpy as np
import tensorflow as tf
import joblib

from schemas.prediction import PredictionResponse

from config.settings import settings



class PredictionService:


    def __init__(self):


        BASE_DIR = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )


        # ==========================================
        # Federated Diabetes Model
        # ==========================================


        federated_model_path = os.path.join(

            BASE_DIR,

            settings.DIABETES_MODEL_PATH

        )


        self.diabetes_model = (
            tf.keras.models.load_model(
                federated_model_path
            )
        )



        # ==========================================
        # Heart Model
        # ==========================================


        heart_model_path = os.path.join(

            BASE_DIR,

            "models",

            "heart_model.pkl"

        )


        self.heart_model = joblib.load(
            heart_model_path
        )



    # ==========================================
    # Diabetes Prediction
    # ==========================================


    def predict_diabetes(
        self,
        data
    ):


        features = np.array([[

            data.pregnancies,

            data.glucose,

            data.blood_pressure,

            data.skin_thickness,

            data.insulin,

            data.bmi,

            data.diabetes_pedigree_function,

            data.age

        ]])


        probability = float(

            self.diabetes_model
            .predict(features)[0][0]

        )


        prediction = (

            1

            if probability >= 0.5

            else 0

        )


        confidence = round(

            probability * 100,

            2

        )


        return PredictionResponse(

            disease="Diabetes",

            prediction=(

                "Positive"

                if prediction == 1

                else "Negative"

            ),

            probability=confidence

        ).model_dump()



    # ==========================================
    # Heart Prediction
    # ==========================================


    def predict_heart(
        self,
        data
    ):


        features = np.array([[

            data.age,

            data.sex,

            data.cp,

            data.trestbps,

            data.chol,

            data.fbs,

            data.restecg,

            data.thalach,

            data.exang,

            data.oldpeak,

            data.slope,

            data.ca,

            data.thal

        ]])


        prediction = (
            self.heart_model
            .predict(features)[0]
        )


        probability = (
            self.heart_model
            .predict_proba(features)[0]
        )


        confidence = round(

            float(max(probability)) * 100,

            2

        )


        return PredictionResponse(

            disease="Heart Disease",

            prediction=(

                "Positive"

                if prediction == 1

                else "Negative"

            ),

            probability=confidence

        ).model_dump()