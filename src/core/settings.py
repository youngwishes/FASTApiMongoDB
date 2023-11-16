from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    MONGO_USERNAME: str = Field("mongo", title="Имя пользователя")
    MONGO_HOST: str = Field("localhost", title="Хост")
    MONGO_PASSWORD: str = Field("mongo", title="Пароль")
    MONGO_DB: str = Field("forms", title="Название базы данных")
    MONGO_PORT: int = Field(27017, title="Порт для подключения к MongoDB")
    MONGO_DRIVER: str = "mongodb"
    AUTHENTICATION_DATABASE: str = Field("admin", title="БД для аутентификации клиента")

    @property
    def mongodb_uri(self):
        return (
            f"{self.MONGO_DRIVER}://{self.MONGO_USERNAME}:{self.MONGO_PASSWORD}"
            f"@{self.MONGO_HOST}/{self.MONGO_DB}?authSource={self.AUTHENTICATION_DATABASE}"
        )


def get_settings(env_file: str = ".env") -> Settings:
    return Settings(_env_file=env_file)
