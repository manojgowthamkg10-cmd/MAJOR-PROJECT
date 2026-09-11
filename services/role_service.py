from database.firestore import get_firestore

from utils.constants import PATIENT_ROLE



class RoleService:


    def __init__(self):

        self.db = get_firestore()



    def update_role(
        self,
        uid: str,
        role: str
    ):


        allowed_roles = [

            "PATIENT",

            "DOCTOR",

            "HOSPITAL",

            "ADMIN"

        ]


        if role not in allowed_roles:

            raise Exception(
                "Invalid role"
            )


        self.db.collection(
            "users"
        ).document(uid).update(

            {
                "role": role
            }

        )


        return {

            "uid": uid,

            "role": role

        }



    def get_user_role(
        self,
        uid: str
    ):


        user = (

            self.db.collection("users")

            .document(uid)

            .get()

        )


        if not user.exists:

            raise Exception(
                "User not found"
            )


        data = user.to_dict()


        return {

            "uid": uid,

            "role": data.get(
                "role",
                PATIENT_ROLE
            )

        }