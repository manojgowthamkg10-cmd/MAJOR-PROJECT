from schemas.bmi import BMIResponse


class BMIService:
    """
    BMI Service
    Calculates BMI and provides
    basic health guidance.
    """


    @staticmethod
    def calculate_bmi(
        height_cm: float,
        weight_kg: float
    ) -> dict:


        height_m = height_cm / 100


        bmi = weight_kg / (height_m ** 2)

        bmi = round(
            bmi,
            2
        )


        if bmi < 18.5:

            category = "Underweight"

            health_status = (
                "Body weight is below the healthy range"
            )

            risk_level = "Moderate"


            recommendations = [
                "Maintain balanced nutrition",
                "Increase healthy calorie intake",
                "Include strength training"
            ]


        elif bmi < 25:

            category = "Normal"

            health_status = (
                "Body weight is within healthy range"
            )

            risk_level = "Low"


            recommendations = [
                "Continue balanced diet",
                "Maintain regular exercise",
                "Monitor health regularly"
            ]


        elif bmi < 30:

            category = "Overweight"

            health_status = (
                "Body weight is above healthy range"
            )

            risk_level = "Moderate"


            recommendations = [
                "Increase physical activity",
                "Maintain calorie balance",
                "Monitor weight regularly"
            ]


        elif bmi < 35:

            category = "Obesity Class I"

            health_status = (
                "Higher health risk due to increased BMI"
            )

            risk_level = "High"


            recommendations = [
                "Follow structured weight management",
                "Exercise regularly",
                "Consult healthcare professionals"
            ]


        elif bmi < 40:

            category = "Obesity Class II"

            health_status = (
                "Significantly increased health risk"
            )

            risk_level = "High"


            recommendations = [
                "Create a supervised lifestyle plan",
                "Monitor metabolic health",
                "Seek professional guidance"
            ]


        else:

            category = "Obesity Class III"

            health_status = (
                "Very high BMI requiring health monitoring"
            )

            risk_level = "Very High"


            recommendations = [
                "Consult healthcare professionals",
                "Follow personalized health plan",
                "Monitor chronic disease risks"
            ]



        return BMIResponse(

            bmi=bmi,

            category=category,

            health_status=health_status,

            risk_level=risk_level,

            recommendations=recommendations

        ).model_dump()