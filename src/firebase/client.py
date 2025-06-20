import json
import os
from typing import Dict

from firebase_admin import credentials, initialize_app, messaging, get_app

from src.firebase.exceptions import FirebaseInitError


def initialize_firebase_app():
    """Initialize Firebase Admin SDK if not already initialized."""
    try:
        get_app()
    except ValueError:
        try:
            # Get Firebase credentials JSON content from environment variable
            firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")

            if not firebase_credentials:
                raise ValueError("FIREBASE_CREDENTIALS environment variable is not set")

            try:
                # Parse the JSON content from the environment variable
                creds_dict = json.loads(firebase_credentials)
                # Initialize with credentials dictionary
                cred = credentials.Certificate(creds_dict)
                initialize_app(cred)
            except json.JSONDecodeError:
                raise ValueError("FIREBASE_CREDENTIALS environment variable contains invalid JSON")

        except Exception as e:
            raise FirebaseInitError(f"Failed to initialize Firebase: {str(e)}")


async def send_firebase_multicast(tokens: list[str], data: Dict[str, str]):
    """Send a multicast message to multiple devices."""
    message = messaging.MulticastMessage(
        data=data,
        tokens=tokens
    )
    return messaging.send_each_for_multicast(message)
