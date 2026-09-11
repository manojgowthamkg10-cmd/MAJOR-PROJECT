from datetime import datetime
import uuid

from database.hospital_repository import HospitalRepository


class HospitalService:

    def __init__(self):
        self.repository = HospitalRepository()

    def create_hospital(self, hospital):

        hospital_id = str(uuid.uuid4())

        hospital_data = {
            "hospital_id": hospital_id,
            "hospital_name": hospital.hospital_name,
            "hospital_code": hospital.hospital_code,
            "location": hospital.location,
            "contact_email": hospital.contact_email,
            "contact_phone": hospital.contact_phone,
            "status": "Active",
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat(),
        }

        self.repository.create_hospital(
            hospital_id,
            hospital_data,
        )

        return hospital_data

    def get_hospital(self, hospital_id: str):
        return self.repository.get_hospital(hospital_id)

    def get_all_hospitals(self):
        return self.repository.get_all_hospitals()

    def update_hospital(self, hospital_id: str, data: dict):
        data["updated_at"] = datetime.utcnow().isoformat()

        self.repository.update_hospital(
            hospital_id,
            data,
        )

        return self.get_hospital(hospital_id)

    def delete_hospital(self, hospital_id: str):
        self.repository.delete_hospital(hospital_id)
        return {"message": "Hospital deleted successfully"}