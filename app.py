from datetime import datetime
from pymongo import MongoClient, ASCENDING

import queries as q

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

q.insert_friend(collection, name="Debora Catalan Bonilla", birthday=datetime(1997, 3, 27))
#q.remove_friend_by_name(collection, "Yolanda Almazan Perez")
q.check_friends(collection)