from typing import List

from src.firebase.client import send_firebase_multicast

from src.invitations.schemas import InvitationRequest, InvitationResponse, MessageResponse


async def send_invitation(request: InvitationRequest) -> InvitationResponse:
    """Send invitation via Firebase Cloud Messaging."""
    # Map request data to Firebase message format
    data_dict = {
        "type": request.data.type,
        "meeting_type": request.data.meeting_type,
        "first_name": request.data.first_name,
        "last_name": request.data.last_name,
        "email": request.data.email,
        "inviter_token": request.data.inviter_token,
        "meeting_room_id": request.data.meeting_room_id,
    }

    # Send message using Firebase client
    response = await send_firebase_multicast(request.registration_ids, data_dict)

    # Process response
    message_responses: List[MessageResponse] = []
    for resp in response.responses:
        if resp.success:
            message_responses.append(
                MessageResponse(success=True, message_id=resp.message_id)
            )
        else:
            message_responses.append(
                MessageResponse(success=False, error=str(resp.exception))
            )

    return InvitationResponse(
        success=True,
        success_count=response.success_count,
        failure_count=response.failure_count,
        responses=message_responses
    )
