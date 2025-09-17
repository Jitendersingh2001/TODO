from pydantic import BaseSettings

class AppSettings(BaseSettings):
    APP_NAME: str
    APP_ENV: str = "development"
    APP_DEBUG: bool = True
    APP_PORT: int = 8000

class DatabaseSettings(BaseSettings):
    DB_CONNECTION: str
    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str

    @property
    def URL(self) -> str:
        """Return full SQLAlchemy database URL."""
        return (
            f"{self.DB_CONNECTION}+pymysql://{self.DB_USERNAME}:"
            f"{self.DB_PASSWORD}@{self.DB_HOST}:"
            f"{self.DB_PORT}/{self.DB_DATABASE}"
        )

class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    db: DatabaseSettings = DatabaseSettings()

    class Config:
        env_file = ".env"
        case_sensitive = True
        env_nested_delimiter = "__"

settings = Settings()
