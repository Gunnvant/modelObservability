import sys
import os


parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(parent_dir)

import mongoDBService.core as core
from mongoDBService.entities import DriftReport

mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_host = os.getenv("MONGO_HOST")
mongo_db = os.getenv("MONGO_DB")
mongo_collection = os.getenv("MONGO_COLLECTION")

db_service = core.MongoDBService(
    host="localhost",
    user=None,
    password=None,
    dbname="monitoring",
    collection="drift",
)
