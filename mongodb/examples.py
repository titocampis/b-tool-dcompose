import os
from datetime import datetime

from pymongo import MongoClient

from mongodb import filters as f
from mongodb import internal_queries as q

# Get MongoDB connection details from environment variables
mongo_host = os.getenv("MONGO_HOST", "localhost")
mongo_port = int(os.getenv("MONGO_PORT", "27017"))

# Defining database
client = MongoClient(mongo_host, mongo_port)
db = client["friends_birthdays"]
friends_collection = db["friends_friends_collection"]

# INSERTS AND UPDATES
q.insert_friend(
    friends_collection,
    "jiminy cricket gepeto",
    birthday=datetime(1950, 1, 1, 0, 0),
    sex=True,
    alias="pinocho",
    phone="123456789",
)
q.insert_friend_dict(
    friends_collection,
    {
        "name": "Jiminy Cricket Gepeto",
        "birthday": datetime(1950, 1, 1, 0, 0),
        "sex": True,
        "alias": "Pinocho",
        "phone": "123456789",
        "month": "january",
        "day": 1,
        "month_number": 1,
    },
)
q.update_by_name(friends_collection, "jiminy cricket gepeto", "sex", False)
q.update_by_name(
    friends_collection,
    "jiminy cricket gepeto",
    "birthday",
    datetime(1950, 1, 1, 0, 0),
)
q.update_by_name(
    friends_collection, "jiminy cricket gepeto", "phone", "123456789"
)
q.update_by_name(
    friends_collection, "jiminy cricket gepeto", "alias", "pinocho"
)
q.remove_friend_by_name(friends_collection, "jiminy cricket gepeto")

# GETTERS
print(f.get_friend_by_alias(friends_collection, "pinocho"))
print(f.get_friend_by_name(friends_collection, "jiminy cricket gepeto"))
print(f.get_friends(friends_collection))
print(f.get_birthdays_by_month(friends_collection, "january"))
