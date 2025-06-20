import json
import os
import logging
from typing import Dict
from pathlib import Path

from firebase_admin import credentials, initialize_app, messaging, get_app

# Updated import path to use the new module
from firebase_service.exceptions import FirebaseInitError


def initialize_firebase_app():
    """Initialize Firebase Admin SDK if not already initialized."""
    try:
        # Check if app is already initialized
        get_app()
        logging.info("Firebase app already initialized")
    except ValueError:
        try:
            # First try: Get Firebase credentials from environment variable
            firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")

            if firebase_credentials:
                try:
                    # Parse the JSON content from the environment variable
                    creds_dict = json.loads(firebase_credentials)
                    # Initialize with credentials dictionary
                    cred = credentials.Certificate(creds_dict)
                    initialize_app(cred)
                    logging.info("Firebase initialized with credentials from environment variable")
                    return
                except json.JSONDecodeError:
                    logging.warning("FIREBASE_CREDENTIALS environment variable contains invalid JSON, trying credentials file...")

        except Exception as e:
            raise FirebaseInitError(f"Failed to initialize Firebase: {str(e)}")


async def send_firebase_multicast(tokens: list[str], data: Dict[str, str]):
    """Send a multicast message to multiple devices."""
    message = messaging.MulticastMessage(
        data=data,
        tokens=tokens
    )
    return messaging.send_each_for_multicast(message)
