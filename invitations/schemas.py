from typing import List, Optional, Any
import json

from pydantic import BaseModel, model_validator


class InvitationData(BaseModel):
    type: str
    meeting_type: str
    first_name: str
    last_name: str
    email: str
    inviter_token: str
    meeting_room_id: str


class InvitationResponseData(BaseModel):
    type: str
    action: str
    meeting_room_id: str


class InvitationActionRequest(BaseModel):
    registration_ids: List[str]
    data: InvitationResponseData

    @model_validator(mode='before')
    @classmethod
    def parse_json_from_string(cls, value: Any) -> Any:
        if isinstance(value, str):
            return json.loads(value)
        return value


class InvitationRequest(BaseModel):
    registration_ids: List[str]
    data: InvitationData

    @model_validator(mode='before')
    @classmethod
    def parse_json_from_string(cls, value: Any) -> Any:
        if isinstance(value, str):
            return json.loads(value)
        return value


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
