from dataclasses import asdict, dataclass
from os import getenv

from dotenv import find_dotenv
from pydantic import Field, model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    HOST: str = Field(default='HOST')
    PROJECT_NAME: str = Field(default='PROJECT_NAME')
    LOG_DIR: str = Field(default='LOG_DIR')
    V1: str = Field(default='V1')
    HTTP_SECURE: str = Field(default='HTTP_SECURE')
    HTTP_PORT: int = Field(default=80)
    ENVIRONMENT: str = Field(default='ENVIRONMENT')

    DB_HOST: str = Field(default='DB_HOST')
    DB_PASS: str = Field(default='DB_PASS')
    DB_PORT: str = Field(default='DB_PORT')
    DB_USER: str = Field(default='DB_USER')
    DB_NAME: str = Field(default='DB_NAME')
    DB_URL: str = Field(default='DB_URL')

    class Config:
        validate_assignment = True


settings = Settings()
