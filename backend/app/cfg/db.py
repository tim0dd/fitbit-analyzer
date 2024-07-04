from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient

_mongo_client: Optional[AgnosticClient] = None


def get_mongodb():
    global _mongo_client
    if not _mongo_client:
        _mongo_client = AsyncIOMotorClient("mongodb://localhost:27017")
    return _mongo_client.db


def close_mongo_client():
    global _mongo_client
    if _mongo_client:
        _mongo_client.close()
