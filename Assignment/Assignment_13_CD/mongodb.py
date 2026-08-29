from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:1800"
)

db = client.pluto

posts = db.posts


def write():

    posts.insert_one(
        {
            "message":
                "MongoDB working"
        }
    )


write()

print(
    "Document inserted into MongoDB."
)