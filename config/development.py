from .settings import Settings


class DevelopmentSettings(Settings):
    DEBUG: bool = True
    ALLOWED_HOSTS: list[str] = ["*"]

    DATABASE_URL: str = "sqlite:///dev.db"
    DATABASE_NAME: str = "dev.db"
    DATABASE_USER: str = ""
    DATABASE_PASSWORD: str = ""
    DATABASE_HOST: str = ""
    DATABASE_PORT: str = ""

    LOGGING_LEVEL: str = "DEBUG"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


development_settings = DevelopmentSettings()
