from database.firestore import get_firestore


class HospitalRepository:

    def __init__(self):
        self.db = get_firestore()

    def create_hospital(self, hospital_id: str, hospital_data: dict):
        self.db.collection("hospitals").document(hospital_id).set(hospital_data)

    def get_hospital(self, hospital_id: str):
        document = (
            self.db.collection("hospitals")
            .document(hospital_id)
            .get()
        )

        if document.exists:
            return document.to_dict()

        return None

    def get_all_hospitals(self):
        docs = self.db.collection("hospitals").stream()

        hospitals = []

        for doc in docs:
            hospitals.append(doc.to_dict())

        return hospitals

    def update_hospital(self, hospital_id: str, data: dict):
        self.db.collection("hospitals").document(hospital_id).update(data)

    def delete_hospital(self, hospital_id: str):
        self.db.collection("hospitals").document(hospital_id).delete()