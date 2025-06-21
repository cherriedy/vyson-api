from fastapi import APIRouter, status

from invitations.exceptions import InvalidInvitationData, FirebaseMessageError
from invitations.schemas import InvitationRequest, InvitationResponse, InvitationActionRequest
from invitations.service import send_invitation, send_invitation_response

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


@router.post(
    "/accept",
    response_model=InvitationResponse,
    status_code=status.HTTP_200_OK,
    summary="Accept an invitation",
    description="Sends an FCM notification to accept an invitation"
)
async def accept_invitation_endpoint(request: InvitationActionRequest):
    try:
        if not request.registration_ids:
            raise InvalidInvitationData("registration_ids must not be empty")
        return await send_invitation_response(request, "accept")
    except Exception as e:
        raise FirebaseMessageError(str(e))


@router.post(
    "/cancel",
    response_model=InvitationResponse,
    status_code=status.HTTP_200_OK,
    summary="Cancel an invitation",
    description="Sends an FCM notification to cancel an invitation"
)
async def cancel_invitation_endpoint(request: InvitationActionRequest):
    try:
        if not request.registration_ids:
            raise InvalidInvitationData("registration_ids must not be empty")
        return await send_invitation_response(request, "cancel")
    except Exception as e:
        raise FirebaseMessageError(str(e))


@router.post(
    "/reject",
    response_model=InvitationResponse,
    status_code=status.HTTP_200_OK,
    summary="Reject an invitation",
    description="Sends an FCM notification to reject an invitation"
)
async def reject_invitation_endpoint(request: InvitationActionRequest):
    try:
        if not request.registration_ids:
            raise InvalidInvitationData("registration_ids must not be empty")
        return await send_invitation_response(request, "reject")
    except Exception as e:
        raise FirebaseMessageError(str(e))
