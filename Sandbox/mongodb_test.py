import pymongo
from pymongo import MongoClient

try:

    client = MongoClient(
        "mongodb://localhost:27017"
    )

    db = client.pluto

    collection = db.posts

    count = collection.count_documents({})

    print("MongoDB connection successful.")
    print(f"Documents: {count}")

except Exception as e:

    print(f"MongoDB Error: {e}")