from functools import lru_cache

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    APP_NAME: str = "Invitation Service"
    APP_DESCRIPTION: str = "API for sending invitations via Firebase Cloud Messaging"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


@lru_cache()
def get_app_settings() -> AppSettings:
    return AppSettings()
