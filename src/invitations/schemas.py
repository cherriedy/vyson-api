from typing import List, Optional

from pydantic import BaseModel, Field


class InvitationData(BaseModel):
    type: str
    meeting_type: str
    first_name: str
    last_name: str
    email: str
    inviter_token: str
    meeting_room_id: str


class InvitationRequest(BaseModel):
    registration_ids: List[str]
    data: InvitationData


class MessageResponse(BaseModel):
    success: bool
    message_id: Optional[str] = None
    error: Optional[str] = None


class InvitationResponse(BaseModel):
    success: bool
    success_count: Optional[int] = None
    failure_count: Optional[int] = None
    responses: Optional[List[MessageResponse]] = None
    error: Optional[str] = None
