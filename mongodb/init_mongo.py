import os

from pymongo import MongoClient

from mongodb import internal_queries as q

# Get MongoDB connection details from environment variables
mongo_host = os.getenv("MONGO_HOST", "localhost")
mongo_port = int(os.getenv("MONGO_PORT", "27017"))

# Defining database
client = MongoClient(mongo_host, mongo_port)
db = client["friends_birthdays"]
friends_collection = db["friends_collection"]

# Set the name field as unique
friends_collection.create_index([("name", 1)], unique=True)
# q.create_birthday_index(friends_collection)

# Get indexes
q.print_indexes(friends_collection)
