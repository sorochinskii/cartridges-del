from dotenv import find_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    def __init__(self, env_file):
        super().__init__(_env_file=env_file, _case_sensitive=True, )

    HOST: str = Field(default='HOST')
    SSH_USER: str = Field(default='SSH_USER')
    SSH_PRIVATE_KEY: str = Field(default='SSH_KEY')
    SSH_PASSPHRASE: str = Field(default='SSH_PASSPHRASE')
    SSH_PORT: str = Field(default='SSH_PORT')
    PROJECT_NAME: str = Field(default='PROJECT_NAME')
    LOG_DIR: str = Field(default='LOG_DIR')
    V1: str = Field(default='V1')
    HTTP_SECURE: str = Field(default='HTTP_SECURE')
    HTTP_PORT: int = Field(default=80)

    # DB_HOST: str = Field(default='DB_HOST')
    # DB_PASS: str = Field(default='DB_PASS')
    # DB_PORT: str = Field(default='DB_PORT')
    # DB_USER: str = Field(default='DB_USER')
    # DB_NAME: str = Field(default='DB_NAME')
    # DB_URL: str = Field(default='DB_URL')

    class Config:
        validate_assignment = True


envs = find_dotenv('.env', raise_error_if_not_found=True)
settings = Settings(env_file=envs)
