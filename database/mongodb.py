import pymongo
from dotenv import load_dotenv
load_dotenv()
import os

host = os.getenv("MONGO_HOST")
DEV = os.getenv("DEV")
client = pymongo.MongoClient("mongodb://44.209.61.209:27017/") if DEV == "DEV" else pymongo.MongoClient(host)
db = client["xfiv-incoming-access"]
print(db.list_collection_names())