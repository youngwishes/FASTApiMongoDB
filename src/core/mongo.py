from motor import motor_asyncio
from motor.motor_asyncio import AsyncIOMotorCollection
from src.core import get_settings

settings = get_settings()
client = motor_asyncio.AsyncIOMotorClient(settings.mongodb_uri)

database = client.get_database("forms")


async def get_collection() -> AsyncIOMotorCollection:
    return database.get_collection(name="forms")
