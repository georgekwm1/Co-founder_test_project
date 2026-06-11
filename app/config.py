from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    database_url: str
    api_key: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    redis_url: str
    email_host: str
    email_port: int
    email_host_user: str
    email_host_password: str
    sender_email: str

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / ".env",
    )

settings = Settings()