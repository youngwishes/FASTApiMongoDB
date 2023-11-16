from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    MONGO_USERNAME: str = Field("mongo")
    MONGO_HOST: str = Field("localhost")
    MONGO_PASSWORD: str = Field("mongo")
    MONGO_DB: str = Field("forms")
    MONGO_PORT: int = Field(27017)
    MONGO_DRIVER: str = "mongodb"

    @property
    def mongodb_uri(self):
        return (
            f"{self.MONGO_DRIVER}://{self.MONGO_USERNAME}:{self.MONGO_PASSWORD}@{self.MONGO_HOST}/{self.MONGO_DB}"
        )


def get_settings(env_file: str = ".env") -> Settings:
    return Settings(_env_file=env_file)
