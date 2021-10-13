import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config

MONGO_DETAILS = config('MONGO_DETAILS') # read environment variable.
print(MONGO_DETAILS)

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.nippet_main