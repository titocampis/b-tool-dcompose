from datetime import datetime
from pymongo import MongoClient, ASCENDING

import queries as q

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

q.insert_friend(collection, name="Mario Alcaide Almazán", birthday=datetime(2006, 5, 8))
#q.remove_friend_by_name(collection, "Mario Alcaide Almazán")
q.check_friends(collection)