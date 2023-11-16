import motor.motor_asyncio
from src.core import get_settings

settings = get_settings()
client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_uri)

database = client.get_database("forms")
forms_collection = database.get_collection("forms")
