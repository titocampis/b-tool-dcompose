from pymongo import MongoClient, ASCENDING

import filters as q

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

# Set the name field as unique
collection.create_index([('name', 1)], unique=True)
# q.create_birthday_index(collection)

# Get indexes
q.get_indexes(collection)
