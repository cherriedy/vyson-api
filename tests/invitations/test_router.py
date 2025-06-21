import pytest
from unittest.mock import AsyncMock, patch
from httpx import AsyncClient, ASGITransport
from fastapi import status

from main import app  # Assuming your FastAPI app instance is named app in main.py


@pytest.mark.asyncio
@patch("invitations.router.send_invitation_response", new_callable=AsyncMock)
async def test_accept_invitation_endpoint(mock_send_invitation_response):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # Arrange
        request_data = {
            "registration_ids": ["test_token"],
            "data": {
                "type": "response",
                "action": "accept",
                "meeting_room_id": "room_123"
            }
        }
        mock_send_invitation_response.return_value = {
            "success": True,
            "success_count": 1,
            "failure_count": 0,
            "responses": []
        }

        # Act
        response = await ac.post("/api/v1/invitations/accept", json=request_data)

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "success": True,
            "success_count": 1,
            "failure_count": 0,
            "responses": [],
            "error": None
        }
        mock_send_invitation_response.assert_called_once()


@pytest.mark.asyncio
@patch("invitations.router.send_invitation_response", new_callable=AsyncMock)
async def test_cancel_invitation_endpoint(mock_send_invitation_response):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # Arrange
        request_data = {
            "registration_ids": ["test_token"],
            "data": {
                "type": "response",
                "action": "cancel",
                "meeting_room_id": "room_123"
            }
        }
        mock_send_invitation_response.return_value = {
            "success": True,
            "success_count": 1,
            "failure_count": 0,
            "responses": []
        }

        # Act
        response = await ac.post("/api/v1/invitations/cancel", json=request_data)

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "success": True,
            "success_count": 1,
            "failure_count": 0,
            "responses": [],
            "error": None
        }
        mock_send_invitation_response.assert_called_once()


@pytest.mark.asyncio
@patch("invitations.router.send_invitation_response", new_callable=AsyncMock)
async def test_reject_invitation_endpoint(mock_send_invitation_response):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # Arrange
        request_data = {
            "registration_ids": ["test_token"],
            "data": {
                "type": "response",
                "action": "reject",
                "meeting_room_id": "room_123"
            }
        }
        mock_send_invitation_response.return_value = {
            "success": True,
            "success_count": 1,
            "failure_count": 0,
            "responses": []
        }

        # Act
        response = await ac.post("/api/v1/invitations/reject", json=request_data)

        # Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "success": True,
            "success_count": 1,
            "failure_count": 0,
            "responses": [],
            "error": None
        }
        mock_send_invitation_response.assert_called_once()
