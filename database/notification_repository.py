from database.firestore import get_firestore


class NotificationRepository:


    def __init__(self):

        self.db = get_firestore()



    def save_notification(
        self,
        notification_data: dict
    ):

        doc = (
            self.db.collection("notifications")
            .document()
        )


        notification_data["notification_id"] = doc.id


        doc.set(notification_data)


        return notification_data



    def get_user_notifications(
        self,
        uid: str
    ):


        docs = (

            self.db.collection("notifications")

            .where(
                "uid",
                "==",
                uid
            )

            .stream()

        )


        notifications = []


        for doc in docs:

            notifications.append(
                doc.to_dict()
            )


        return notifications