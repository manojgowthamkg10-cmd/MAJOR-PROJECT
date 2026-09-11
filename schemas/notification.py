from pydantic import BaseModel
from typing import List


class NotificationResponse(BaseModel):

    notification_id: str

    title: str

    message: str

    severity: str

    notification_type: str



class NotificationListResponse(BaseModel):

    notifications: List[NotificationResponse]