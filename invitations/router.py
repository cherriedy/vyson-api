from fastapi import APIRouter, status

from invitations.exceptions import InvalidInvitationData, FirebaseMessageError
from invitations.schemas import InvitationRequest, InvitationResponse
from invitations.service import send_invitation

router = APIRouter(prefix="/invitations", tags=["invitations"])


@router.post(
    "/send",
    response_model=InvitationResponse,
    status_code=status.HTTP_200_OK,
    summary="Send invitation to multiple devices",
    description="Sends FCM notification with invitation details to provided devices"
)
async def send_invitation_endpoint(request: InvitationRequest):
    try:
        if not request.registration_ids:
            raise InvalidInvitationData("registration_ids must not be empty")

        return await send_invitation(request)
    except Exception as e:
        raise FirebaseMessageError(str(e))
