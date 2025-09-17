from pydantic_settings import BaseSettings
from urllib.parse import quote_plus

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
    def DB_DATABASE_URL(self) -> str:
        # URL encode the password
        password = quote_plus(self.DB_PASSWORD)
        return f"{self.DB_CONNECTION}+pymysql://{self.DB_USERNAME}:{password}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}"

class Settings(BaseSettings):
    app: AppSettings
    db: DatabaseSettings

    class Config:
        env_file = ".env"
        case_sensitive = True
        env_nested_delimiter = "__"

settings = Settings()
