from typing import Self
from pydantic import Field, SecretStr, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


class DatabaseConfig(BaseConfig):
    model_config = SettingsConfigDict(env_prefix="POSTGRES_")

    HOST: str = "localhost"
    PORT: int = 5432
    DB: str
    USER: str
    PASSWORD: SecretStr

    @computed_field
    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.USER}:{self.PASSWORD.get_secret_value()}"
            f"@{self.HOST}:{self.PORT}/{self.DB}"
        )


class Config(BaseSettings):
    db: DatabaseConfig = Field(default_factory=DatabaseConfig)

    @classmethod
    def load(cls) -> Self:
        return cls()


config = Config.load()
