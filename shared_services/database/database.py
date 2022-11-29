import os

from motor import motor_asyncio

from app.services import config_service

# Returns a db client connected to the database name specified in the config


async def get_client():
    config_service.load_config()
    mongo_user = os.environ.get("db_username")
    mongo_password = os.environ.get("db_password")
    mongo_url = os.environ.get("db_url")
    mongo_uri = f"mongodb+srv://{mongo_user}:{mongo_password}@{mongo_url}"
    client = motor_asyncio.AsyncIOMotorClient(mongo_uri)
    return client


async def get_database():
    mongo_db_name = os.environ.get("db_name")
    return mongo_db_name
