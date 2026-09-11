from pydantic import BaseModel


class RoleUpdateRequest(BaseModel):

    uid: str

    role: str