from pymongo import MongoClient, ASCENDING

import queries as q

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["friends_birthdays"]
collection = db["friends_collection"]

# Set the name field as unique
q.create_unique_index(collection, field="name")

# Check indexes
q.check_indexes(collection)