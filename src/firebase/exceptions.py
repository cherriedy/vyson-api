from fastapi import HTTPException, status


class FirebaseInitError(Exception):
    """Exception raised when Firebase initialization fails."""
    pass


class FirebaseOperationError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Firebase operation failed: {detail}"
        )
