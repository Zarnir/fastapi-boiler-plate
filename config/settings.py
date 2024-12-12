from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    DEBUG: bool
    ALLOWED_HOSTS: list[str]

    DATABASE_URL: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str

    LOGGING_LEVEL: str

    API_PREFIX: str = "/api"
    API_VERSION: str = "v1"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
