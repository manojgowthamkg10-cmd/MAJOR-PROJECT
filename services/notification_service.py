from datetime import datetime

from database.notification_repository import NotificationRepository



class NotificationService:


    def __init__(self):

        self.repository = NotificationRepository()



    def create_notification(

        self,

        uid: str,

        title: str,

        message: str,

        severity: str,

        notification_type: str

    ):


        notification = {


            "uid": uid,

            "title": title,

            "message": message,

            "severity": severity,

            "notification_type": notification_type,

            "created_at":
            datetime.utcnow().isoformat()

        }



        return self.repository.save_notification(
            notification
        )



    def generate_risk_alert(

        self,

        uid: str,

        disease: str,

        probability: float

    ):


        if probability >= 80:


            return self.create_notification(

                uid,

                f"{disease} Risk Alert",

                (
                    f"Your {disease} risk is high. "
                    "Medical monitoring is recommended."
                ),

                "HIGH",

                "RISK_ALERT"

            )


        elif probability >= 50:


            return self.create_notification(

                uid,

                f"{disease} Warning",

                (
                    f"Your {disease} risk is moderate. "
                    "Maintain healthy lifestyle habits."
                ),

                "MEDIUM",

                "RISK_ALERT"

            )


        return None



    def get_notifications(
        self,
        uid: str
    ):

        return self.repository.get_user_notifications(uid)