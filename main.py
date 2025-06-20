import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from config import get_app_settings

from firebase_service.client import initialize_firebase_app
from invitations.router import router as invitations_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    initialize_firebase_app()
    logging.info("Firebase initialized successfully")
    yield
    # Shutdown
    logging.info("Application shutting down")


def create_application() -> FastAPI:
    settings = get_app_settings()

    application = FastAPI(
        title=settings.APP_NAME,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSION,
        debug=settings.DEBUG,
        lifespan=lifespan,
    )

    # Register routers
    application.include_router(invitations_router, prefix="/api/v1")

    return application


app = create_application()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
