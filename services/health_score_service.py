from database.firestore import get_firestore


class HealthScoreService:


    def __init__(self):

        self.db = get_firestore()



    def calculate_score(
        self,
        uid: str
    ):


        profile_doc = (
            self.db.collection("profiles")
            .document(uid)
            .get()
        )


        if not profile_doc.exists:

            raise Exception(
                "Profile not found"
            )


        profile = profile_doc.to_dict()



        factors = {}

        recommendations = []



        # -----------------------------
        # BMI Score
        # -----------------------------

        bmi = profile.get(
            "bmi",
            0
        )


        if 18.5 <= bmi < 25:

            bmi_score = 100

        elif 25 <= bmi < 30:

            bmi_score = 75

            recommendations.append(
                "Work towards maintaining a healthy weight"
            )

        elif bmi >= 30:

            bmi_score = 50

            recommendations.append(
                "Follow a structured weight management plan"
            )

        else:

            bmi_score = 60



        factors["bmi"] = bmi_score



        # -----------------------------
        # Blood Sugar Score
        # -----------------------------

        sugar = profile.get(
            "blood_sugar",
            0
        )


        if sugar <= 100:

            sugar_score = 100

        elif sugar <= 140:

            sugar_score = 75

            recommendations.append(
                "Monitor blood sugar regularly"
            )

        else:

            sugar_score = 50

            recommendations.append(
                "Consult healthcare professionals for sugar management"
            )


        factors["blood_sugar"] = sugar_score



        # -----------------------------
        # Exercise Score
        # -----------------------------

        exercise = profile.get(
            "exercise_per_week",
            0
        )


        if exercise >= 5:

            exercise_score = 100

        elif exercise >= 3:

            exercise_score = 80

        else:

            exercise_score = 50

            recommendations.append(
                "Increase weekly physical activity"
            )


        factors["exercise"] = exercise_score



        # -----------------------------
        # Lifestyle
        # -----------------------------

        lifestyle_score = 100


        if profile.get("smoking"):

            lifestyle_score -= 30

            recommendations.append(
                "Avoid smoking"
            )


        if profile.get("alcohol"):

            lifestyle_score -= 10

            recommendations.append(
                "Reduce alcohol consumption"
            )


        factors["lifestyle"] = lifestyle_score



        # -----------------------------
        # Final Score
        # -----------------------------

        health_score = round(
            sum(factors.values()) / len(factors),
            2
        )



        if health_score >= 80:

            status = "Excellent"

        elif health_score >= 60:

            status = "Good"

        elif health_score >= 40:

            status = "Needs Improvement"

        else:

            status = "High Risk"



        return {

            "health_score": health_score,

            "status": status,

            "factors": factors,

            "recommendations": recommendations

        }