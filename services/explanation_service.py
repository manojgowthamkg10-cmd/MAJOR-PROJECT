class ExplanationService:


    def generate_explanation(
        self,
        disease: str,
        probability: float,
        features: dict
    ):


        risk_factors = []

        recommendations = []



        # Risk calculation

        if probability >= 80:

            risk = "High"

        elif probability >= 50:

            risk = "Moderate"

        else:

            risk = "Low"



        # Diabetes Explanation

        if disease == "Diabetes":


            if features.get("glucose",0) > 140:

                risk_factors.append(
                    "High glucose level"
                )

                recommendations.append(
                    "Monitor blood sugar regularly"
                )


            if features.get("bmi",0) > 25:

                risk_factors.append(
                    "BMI above healthy range"
                )

                recommendations.append(
                    "Maintain healthy weight"
                )


            explanation = (
                "Diabetes risk is influenced by "
                "blood glucose level, BMI and lifestyle factors."
            )



        # Heart Explanation

        elif disease == "Heart Disease":


            if features.get("chol",0) > 200:

                risk_factors.append(
                    "High cholesterol"
                )


            if features.get("age",0) > 45:

                risk_factors.append(
                    "Age-related risk factor"
                )


            recommendations.extend([

                "Maintain heart healthy diet",

                "Exercise regularly",

                "Monitor blood pressure"

            ])


            explanation = (
                "Heart disease risk depends on "
                "cardiac parameters and lifestyle factors."
            )


        else:

            explanation = (
                "Risk analysis generated successfully."
            )



        return {

            "disease": disease,

            "risk_level": risk,

            "explanation": explanation,

            "risk_factors": risk_factors,

            "recommendations": recommendations

        }