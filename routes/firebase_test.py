from datetime import datetime

from fastapi import APIRouter

from database.firestore import get_firestore

router = APIRouter(
    prefix="/firebase",
    tags=["Firebase"],
)


@router.get("/test")
async def firebase_test():
    db = get_firestore()

    db.collection("test").document("connection").set(
        {
            "status": "connected",
            "timestamp": datetime.utcnow().isoformat(),
        }
    )

    return {
        "message": "Firebase connected successfully!"
    }